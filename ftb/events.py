import inspect
import glob
import logging
import sys
import re

from pathlib import Path
from telethon import events

from pymongo import MongoClient
from ftb import mongo2
from ftb import telethn

client = MongoClient()
client = MongoClient(MONGO_DB_URI)
db = client["darkuserbot"]


def register(**args):
    """ Registers a new message. """
    pattern = args.get("pattern", None)

    r_pattern = r"^[/!]"

    if pattern is not None and not pattern.startswith("(?i)"):
        args["pattern"] = "(?i)" + pattern

    args["pattern"] = pattern.replace("^/", r_pattern, 1)

    def decorator(func):
        telethn.add_event_handler(func, events.NewMessage(**args))
        return func

    return decorator
