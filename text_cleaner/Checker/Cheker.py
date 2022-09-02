import re


class CharChecker(object):

    def __init__(self, char, replace_text=''):
        self._chars = char
        self._regex = re.escape(char)
        self._replace_text = replace_text

        self._init_re_pattern()

    def __str__(self):
        return self._chars

    def __repr__(self):
        return self._chars

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
        if isinstance(regex, CharChecker):
            regexes = [self.regex, regex.regex]
        elif isinstance(regex, str):
            regexes = [self.regex] + [re.escape(i) for i in regex]
        elif isinstance(regex, int):
            regexes = [self.regex, f'\\U{regex:0>8X}']
        else:
            raise TypeError(
                'other regex object must be str or CharChecker or int')

        re_pattern = ''.join([regexes])

        return CharChecker(re_pattern, replace_text=self.replace_text)

    def __add__(self, other):
        return self.join_regex(other)

    def __radd__(self, other):
        return self.join_regex(other)

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


class UnicodeRangeChecker(CharChecker):

    def __init__(self, begin, end, replace_text=''):
        self.begin = int(begin)
        self.end = int(end)

        pattern_begin = f'\\U{begin:0>8X}'.encode('utf-8').decode(
            'unicode_escape')
        pattern_end = f'\\U{end:0>8X}'.encode('utf-8').decode('unicode_escape')
        self._regex = f'{re.escape(pattern_begin)}-{re.escape(pattern_end)}'

        self._replace_text = replace_text

        self._init_re_pattern()
