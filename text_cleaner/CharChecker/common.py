from .Checker import UnicodeRangeChecker, RegexChecker

SPACE = RegexChecker(char='\t\n')

GREEK_LETTER_LOWER = UnicodeRangeChecker(0x03b1, 0x03c9)
GREEK_LETTER_UPPER = UnicodeRangeChecker(0x0391, 0x03A6)
GREEK_LETTER = GREEK_LETTER_LOWER + GREEK_LETTER_UPPER