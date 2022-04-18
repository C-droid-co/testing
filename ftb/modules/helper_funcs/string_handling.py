import re
import time
from typing import Dict, List

import bleach
import markdown2
import emoji

from telegram import MessageEntity
from telegram.utils.helpers import escape_markdown

def markdown_parser(
    txt: str,
    entities: Dict[MessageEntity, str] = None,
    offset: int = 0,
) -> str:
    """
    Parse a string, escaping all invalid markdown entities.

    Escapes URL's so as to avoid URL mangling.
    Re-adds any telegram code entities obtained from the entities object.

    :param txt: text to parse
    :param entities: dict of message entities in text
    :param offset: message offset - command and notename length
    :return: valid markdown string
    """
    if not entities:
        entities = {}
    if not txt:
        return ""

    prev = 0
    res = ""
    # Loop over all message entities, and:
    # reinsert code
    # escape free-standing urls
    for ent, ent_text in entities.items():
        if ent.offset < -offset:
            continue

        start = ent.offset + offset  # start of entity
        end = ent.offset + offset + ent.length - 1  # end of entity

        # we only care about code, url, text links
        if ent.type in ("code", "url", "text_link"):
            # count emoji to switch counter
            count = _calc_emoji_offset(txt[:start])
            start -= count
            end -= count

            # URL handling -> do not escape if in [](), escape otherwise.
            if ent.type == "url":
                if any(
                    match.start(1) <= start and end <= match.end(1)
                    for match in LINK_REGEX.finditer(txt)
                ):
                    continue
                # else, check the escapes between the prev and last and forcefully escape the url to avoid mangling
                else:
                    # TODO: investigate possible offset bug when lots of emoji are present
                    res += _selective_escape(txt[prev:start] or "") + escape_markdown(
                        ent_text,
                    )

            # code handling
            elif ent.type == "code":
                res += _selective_escape(txt[prev:start]) + "`" + ent_text + "`"

            # handle markdown/html links
            elif ent.type == "text_link":
                res += _selective_escape(txt[prev:start]) + "[{}]({})".format(
                    ent_text,
                    ent.url,
                )

            end += 1

        # anything else
        else:
            continue

        prev = end

    res += _selective_escape(txt[prev:])  # add the rest of the text
    return res
