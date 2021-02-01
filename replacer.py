# coding: utf-8
import re


class ReplacerError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):

        if self.message:
            return "{0} ".format(self.message)
        else:
            return "Error has been raised"


class Replacer(object):
    def __init__(self, **kwargs):
        self.replacer_character = kwargs.get("replacer_character", "*")
        self.replace_mode = kwargs.get("replace_mode", "middle")
        self.replace_options = {
            "middle": r"(?!^|.$)[^\s]",
            "default": r"(?!^|.$)(.*)",
            "all": r"(.*)",
        }
        if not kwargs.get("reg_pattern", ""):
            raise ReplacerError("Regular expression pattern is missing")
        self.set_reg_pattern(kwargs.get("reg_pattern"))

    def set_reg_pattern(self, pattern):
        self.reg_pattern = pattern

    def callback(self, match):
        match = match.group(1)
        replace_characters = self.replacer_character
        if self.replace_mode != "middle":
            replace_characters = self.replacer_character * len(match)
        return re.sub(
            self.replace_options[self.replace_mode], replace_characters, match
        )

    def replace(self, text):
        return re.sub(self.reg_pattern, self.callback, text, flags=re.IGNORECASE)
