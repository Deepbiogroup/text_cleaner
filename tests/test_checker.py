from text_cleaner.CharChecker import RegexChecker, UnicodeRangeChecker
from text_cleaner.CharChecker.ascii import ASCII_ALPHA_UPPER


def test_checker():
    checker = RegexChecker('a')

    assert str(checker) == 'a'
    assert checker.regex == 'a'
    assert checker.replace_text == ''

    assert checker.keep('abc') == 'a'
    assert checker.remove('abc') == 'bc'
    assert checker.exist('abc') == True
    assert checker.exist('bc') == False
    assert checker.match('aaa') == True
    assert checker.match('abaa') == False
    assert checker.match('bc') == False


def test_checker_add():

    checker = RegexChecker('a')
    checker += '-z'

    assert checker.keep('abc') == 'a'


def test_range():
    assert str(ASCII_ALPHA_UPPER) == 'A-Z'

    assert ASCII_ALPHA_UPPER.keep('ABCabc') == 'ABC'

    assert str(ASCII_ALPHA_UPPER + ASCII_ALPHA_UPPER) == 'A-ZA-Z'
