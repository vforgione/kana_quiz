from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import *


"""
home

about

gojuon
    hiragana
    katakana
"""


def gojuon(request, kana=None):
    plain = Character.objects.filter(is_plain=True, is_dakuten=False, is_yoon=False)
    dakuten = Character.objects.filter(is_dakuten=True, is_yoon=False)
    yoon = Character.objects.filter(is_yoon=True)

    return render_to_response(
        'kana/gojuon.html',
        {
            'plain': plain,
            'dakuten': dakuten,
            'yoon': yoon,
            'kana': kana,
        },
        context_instance=RequestContext(request)
    )
