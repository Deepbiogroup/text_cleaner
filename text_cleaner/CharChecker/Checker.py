import re


class RegexChecker(object):

    def __init__(self, regex=None, char=None, replace_text=''):
        if char:
            if regex: raise ValueError('regex and char ')
            self._regex = re.escape(char)
        else:
            if not regex: raise ValueError('neigher regex or char')
            self._regex = regex

        self._replace_text = replace_text

        self._init_re_pattern()

    def __str__(self):
        return self._regex

    def __repr__(self):
        return self._regex

    @property
    def regex(self):
        return self._regex

    def _init_re_pattern(self):
        self._regex_obj = re.compile(r'[{0}]+'.format(self.regex), re.UNICODE)

    @property
    def replace_text(self):
        return self._replace_text

    def set_replace_text(self, char):
        self._replace_text = char

    def join_regex(self, regex):

        if isinstance(regex, RegexChecker):
            regexes = [self.regex, regex.regex]
        elif isinstance(regex, str):
            regexes = [self.regex, regex]
        elif isinstance(regex, int):
            regexes = [self.regex, re.escape(chr(regex))]
        else:
            raise TypeError(
                'other regex object must be str or RegexChecker or int')

        re_pattern = ''.join(regexes)

        return RegexChecker(regex=re_pattern, replace_text=self.replace_text)

    def add_pattern(self, pattern):

        if isinstance(pattern, RegexChecker):
            return self.join_regex(pattern)
        elif isinstance(pattern, str):
            regexes = [self.regex] + [re.escape(i) for i in pattern]
            return RegexChecker(regex=''.join(regexes),
                                replace_text=self.replace_text)

        elif isinstance(pattern, int):
            return self.join_regex(pattern)
        else:
            raise TypeError(
                'other regex object must be str or RegexChecker or int')

    def __add__(self, other):
        return self.add_pattern(other)

    def __radd__(self, other):
        return self.add_pattern(other)

    def remove(self, text):
        return self._regex_obj.sub(
            self._replace_text,
            text,
        )

    def keep(self, text):
        return self._replace_text.join(
            list(m.group() for m in self._regex_obj.finditer(text)))

    def exist(self, text):
        match = self._regex_obj.match(text)
        return bool(match)

    def match(self, text):
        match = self._regex_obj.match(text)
        if match is None:
            return False
        else:
            return match.group() == text


class UnicodeRangeChecker(RegexChecker):

    def __init__(self, begin, end, replace_text=''):
        assert isinstance(begin, int)
        assert isinstance(end, int)
        assert begin <= end, ValueError(f'begin {begin} >  end {end}')

        begin = chr(begin)
        end = chr(end)

        self._chars = f'{begin}-{end}'
        self._regex = f'{re.escape(begin)}-{re.escape(end)}'
        self._replace_text = replace_text

        self._init_re_pattern()
