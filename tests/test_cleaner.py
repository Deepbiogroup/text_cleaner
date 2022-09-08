from telnetlib import TELNET_PORT
from text_cleaner.Cleaner import TextCleaner


def test_cleaner():
    cleaner = TextCleaner()
    text = '<p><sup>abc</suP>def<br > </p>'
    cleaner.clean(text) == '<sup>abc</sup>def '