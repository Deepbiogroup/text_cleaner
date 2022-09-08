from .Checker import UnicodeRangeChecker


# ascii
ASCII_ALPHA_UPPER = UnicodeRangeChecker(0x0041, 0x005A)
ASCII_ALPHA_LOWER = UnicodeRangeChecker(0x0061, 0x007A)
ASCII_ALPHA = ASCII_ALPHA_UPPER + ASCII_ALPHA_LOWER
ASCII_DIGIT =   UnicodeRangeChecker(0x0030, 0x0039)

ASCII_SYMBOLS_AND_PUNCTUATION = (
    UnicodeRangeChecker(0x0020, 0x002F) +
    UnicodeRangeChecker(0x003A, 0x0040) +
    UnicodeRangeChecker(0x005B, 0x0060) +
    UnicodeRangeChecker(0x007B, 0x007E)
)


ASCII = (
    ASCII_ALPHA +
    ASCII_DIGIT +
    ASCII_SYMBOLS_AND_PUNCTUATION
)

ASCII_ALPHA_UPPER_FULLWIDTH = UnicodeRangeChecker(0xFF21, 0xFF3A)
ASCII_ALPHA_LOWER_FULLWIDTH = UnicodeRangeChecker(0xFF41, 0xFF5A)
ASCII_DIGIT_FULLWIDTH = UnicodeRangeChecker(0xFF10, 0xFF19)

SYMBOLS_AND_PUNCTUATION_EXTENSION = (
    UnicodeRangeChecker(0xFF00, 0xFF0F)  +
    UnicodeRangeChecker(0xFF1A, 0xFF20)  +
    UnicodeRangeChecker(0xFF3B, 0xFF40)  +
    UnicodeRangeChecker(0xFF5B, 0xFF64)  +
    UnicodeRangeChecker(0xFFE0, 0xFFEE)  
)
