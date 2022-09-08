# -*- coding: utf-8 -*-

from .ascii import SYMBOLS_AND_PUNCTUATION_EXTENSION, ASCII
from .Checker import UnicodeRangeChecker

# https://en.wikipedia.org/wiki/CJK_Unified_Ideographs

CJK_COMMON = UnicodeRangeChecker(0x4E00, 0x9FFF)

CJK_EXTENSION = (UnicodeRangeChecker(0x3400, 0x4DFF) +
                 UnicodeRangeChecker(0x20000, 0x2A6DF) +
                 UnicodeRangeChecker(0x2A700, 0x2B73F) +
                 UnicodeRangeChecker(0x2B740, 0x2B81F) +
                 UnicodeRangeChecker(0x2B820, 0x2CEAF))

CJK_COMPATIBILITY = (UnicodeRangeChecker(0x3300, 0x33FF) +
                     UnicodeRangeChecker(0xFE30, 0xFE4F) +
                     UnicodeRangeChecker(0xF900, 0xFAFF) +
                     UnicodeRangeChecker(0x2F800, 0x2FA1F))

# https://gist.github.com/shingchi/64c04e0dd2cbbfbc1350

CJK_SYMBOLS_AND_PUNCTUATION = (
    # http://www.unicode.org/charts/PDF/U3000.pdf
    UnicodeRangeChecker(0x3000, 0x303F) +

    # http://www.unicode.org/charts/PDF/UFF00.pdf
    UnicodeRangeChecker(0xFF00, 0xFFEF) +

    # http://www.unicode.org/charts/PDF/UFE30.pdf
    UnicodeRangeChecker(0xFE30, 0xFE4F))

# processors.

# common usage.
CHINESE_CHARACTER = CJK_COMMON

CHINESE = (ASCII + SYMBOLS_AND_PUNCTUATION_EXTENSION + CJK_COMMON +
           CJK_SYMBOLS_AND_PUNCTUATION)

# full version.
CHINESE_ALL = (CJK_COMMON + CJK_EXTENSION + CJK_COMPATIBILITY +
               CJK_SYMBOLS_AND_PUNCTUATION + SYMBOLS_AND_PUNCTUATION_EXTENSION)
