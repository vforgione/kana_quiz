from django import template
from django.db.models.query import QuerySet

register = template.Library()


@register.tag
def render_as_chart(parser, token):
    bits = token.split_contents()
    try:
        tag = bits.pop(0)
        queryset = parser.compile_filter(bits.pop(0))
    except ValueError:
        raise template.TemplateSyntaxError('%r tag requires a single argument' % token.split_contents()[0])

    return ChartNode(queryset)


class ChartNode(template.Node):

    def __init__(self, queryset):
        self.queryset = queryset

    def render(self, context):
        queryset = self.queryset.resolve(context)
        if not isinstance(queryset, QuerySet):
            raise ValueError(
                '%s requires a QuerySet object - got %s' % (str(self.__class__.__name__), type(queryset)))

        grid = []
        rows = max([char.gojuon_row for char in queryset])
        cols = max([char.gojuon_col for char in queryset])
        for _ in range(rows + 1):
            grid.append([])

        for row in range(rows + 1):
            for col in range(cols + 1):
                try:
                    char = queryset.filter(gojuon_col=col, gojuon_row=row)[0]
                except:
                    char = None
                grid[row].insert(col, char)

        output = ''
        for row in grid:
            for char in row:
                if char:
                    output += '<div class="char">%s</div>' % char.romaji
                else:
                    output += '<div class="char">&nbsp;</div>'
            output += '<br class="clear" />'

        # return '<div><h3>puke</h3></div>'
        return output
