# coding: utf-8
from replacer import Replacer, ReplacerError


class ProfanityReplacer(Replacer):
    def __init__(self, **kwargs):
        """
        Returns an object instance.
        Kwargs:
            - wordfile (list):
            A list of words that will be replaced as a whole word only (no substring search).
            - extra_wordfile (list):
            A list of words that will be replaced if matches are found as word or in-word.
            - replacer_character
            Character used to replace profanity.
            - replace_mode
            How the replacement of profanity will look. Options are: default, middle or all.
        """
        if not kwargs.get("wordfile", ""):
            raise ReplacerError("wordfile is missing")
        wordfiles = []
        if kwargs.get("wordfile", ""):
            wordfiles.append(self.load_wordfile(kwargs.get("wordfile"), r"\b(%s)\b"))
        if kwargs.get("extra_wordfile", ""):
            wordfiles.append(self.load_wordfile(kwargs.get("extra_wordfile"), r"(%s)"))
        kwargs["reg_pattern"] = "(%s)" % r"|".join(map(r"({})".format, wordfiles))
        super(ProfanityReplacer, self).__init__(**kwargs)

    def load_wordfile(self, file_path, pattern):
        word_list = []
        with open(file_path, "r") as f:
            word_list = [line.strip() for line in f.readlines()]
        return pattern % "|".join(word_list)

    def censor(self, text):
        return super(ProfanityReplacer, self).replace(text)
