from django import template
from django.db.models.query import QuerySet

register = template.Library()


@register.tag
def render_as_quiz(parser, token):
    bits = token.split_contents()
    try:
        tag = bits.pop(0)
        queryset = parser.compile_filter(bits.pop(0))
        kana = parser.compile_filter(bits.pop(0))
    except (ValueError, IndexError):
        raise template.TemplateSyntaxError(
            '%r tag requires two arguments: queryset and kana' % token.split_contents()[0])

    return QuizNode(queryset, kana)


class QuizNode(template.Node):

    def __init__(self, queryset, kana):
        self.queryset = queryset
        self.kana = kana

    def render(self, context):
        queryset = self.queryset.resolve(context)
        kana = self.kana.resolve(context)
        if not isinstance(queryset, QuerySet):
            raise ValueError(
                '%s requires a QuerySet object - got %s' % (str(self.__class__.__name__), type(queryset)))

        js_chars = 'var chars = ['
        chars = ', '.join([
            '{ char: "%s", answer: "%s", alternate: "%s" }'
            % (char.__dict__[kana], char.romaji.lower(), str(char.alternate_romaji or '').lower())
            for char in queryset
        ])
        js_chars += chars
        js_chars += '];'
        js_chars_log = 'chars.forEach(function(char){ console.log(char); });'

        js = '<script type="text/javascript">\n'
        js += '\n'.join([
            js_chars, js_chars_log
        ])
        js += '\n</script>'

        return js
