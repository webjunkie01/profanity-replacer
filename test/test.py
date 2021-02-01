# coding: utf-8
import pytest
from profanity_replacer import ProfanityReplacer
from paragraphs import cases, expects
from timeit import default_timer as timer
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


def test_replacer():
    start = timer()
    replacer = ProfanityReplacer(
        wordfile=os.path.join(ROOT_DIR, "wordlist.txt"),
        extra_wordfile=os.path.join(ROOT_DIR, "extra_wordlist.txt"),
        replace_mode="default",
    )
    for i, paragraph in enumerate(cases):
        assert expects[i] == replacer.censor(paragraph)
    end = timer()
    took = end - start
    seconds = took % 60
    print("It took {} seconds".format(seconds))
