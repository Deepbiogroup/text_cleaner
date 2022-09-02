from text_cleaner.Checker.Cheker import CharChecker


def test_checker():
    checker = CharChecker('a')

    assert str(checker) == 'a'
    assert checker.regex == 'a'
    assert checker.replace_text == ''

    assert checker.keep('abc') == 'a'
    assert checker.remove('abc') == 'bc'
    assert checker.exist('abc') == True
    assert checker.exist('bc') == False
    assert checker.match('aaa') == True
    assert checker.match('abaa') == False
