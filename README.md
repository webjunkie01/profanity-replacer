## Profanity Censor

A simple and fast class for censoring profanity in text. It can be used at runtime. It runs on Python 2 and 3.

## How it works.

It needs a list of words that are considered profanity, when this list if provided a search will begin and will 
match the word against the text you want to censor.

This means that for example you want to censor the word `shit` it will search the text for that specific word but will not work for words like `shithead` or `shithole` for example.

For this to work you will have to provide an extra list of words that consider very offensive. Words in this file wil be replaced if they match as a whole word of in-word.

## Example

```
from profanity_replacer import ProfanityReplacer
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# provide this file with words you would like to replace without any word boundaries
very_offensive_words = os.path.join(ROOT_DIR,"extra_wordlist.txt")

replacer = ProfanityReplacer(
    wordfile=os.path.join(ROOT_DIR,'wordlist.txt'), 
    extra_wordfile=very_offensive_words, 
    replace_mode='default')
    sentence = "This place is a fucking shithole"
    censored = replacer.censor(sentece)
    "This place is a f****ing s****hole"
```



