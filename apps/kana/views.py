from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import *


def gojuon(request):
    chars = Character.objects.filter(is_dakuten=False, is_handakuten=False, is_yoon=False)

    grid = []
    rows = max([char.gojuon_row for char in chars])
    cols = max([char.gojuon_col for char in chars])
    for _ in range(rows + 1):
        grid.append([])

    for row in range(rows + 1):
        for col in range(cols + 1):
            try:
                char = chars.filter(gojuon_col=col, gojuon_row=row)[0]
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

    return render_to_response(
        'kana/gojuon.html',
        {
            'chars': output,
            },
        context_instance=RequestContext(request)
    )
