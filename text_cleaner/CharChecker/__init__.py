from .Checker import RegexChecker, UnicodeRangeChecker
from .ascii import ASCII
from .chinese import CHINESE
from .common import GREEK_LETTER, SPACE

valid_char_checker = ASCII + GREEK_LETTER + SPACE