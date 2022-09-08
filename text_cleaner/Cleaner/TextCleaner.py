import logging
import re
from .trans_table import translate_table

logger = logging.getLogger('TextCleaner')


class TextCleaner:

    def __init__(self, ) -> None:
        self._translate_table = translate_table
        self._keep_html_tags = ['sub', 'sup']
        self._remove_html_tag_pair = [
            'em', 'i', 'italic', 'strong', 'p', 'a', 'span', 'b', 'u'
        ]
        self._remove_html_tag_single = ['br', 'wb', 'w/br']

    def char_replace(self, text):
        return text.translate(self._translate_table)

    def remove_html_tag(self, text):
        for tag in self._remove_html_tag_single:
            if f'<{tag}' not in text.lower(): continue
            text = re.sub(f'<{re.escape(tag)}\\s*/?>', '', text, re.I)

        for tag in self._keep_html_tags:
            if f'<{tag}' not in text.lower(): continue
            text = re.sub(f'<{re.escape(tag)}\\b.*>',
                          f'<{tag}>',
                          text,
                          flags=re.I)
            text = re.sub(f'</{re.escape(tag)}>',
                          f'</{tag}>',
                          text,
                          flags=re.I)
        for tag in self._remove_html_tag_pair:
            if f'<{tag}' not in text.lower() and f'</{tag}' not in text.lower(
            ):
                continue
            if (not re.findall(f'<{re.escape(tag)}\\b.*?>', text, re.I)) or (
                    not re.findall(f'</{re.escape(tag)}\\s*?>', text, re.I)):
                logger.warning(f'html tag {tag} has no close tag.')
            text = re.sub(f'<{re.escape(tag)}\\b.*?>', '', text, flags=re.I)
            text = re.sub(f'</{re.escape(tag)}\\s*?>', '', text, flags=re.I)

        return text

    def clean(self, text):
        text = self.remove_html_tag(text)
        text = self.char_replace(text)
        text = re.sub(r'\n+', '\n', text, flags=re.DOTALL)

        return text

    def remove_space(self, text):
        text = re.sub(r'\s+', ' ', text, flags=re.DOTALL)

        return text