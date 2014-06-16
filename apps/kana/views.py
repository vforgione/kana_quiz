from django.db.models import Q
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import *


def home(request):
    return render_to_response(
        'kana/home.html', {}, context_instance=RequestContext(request)
    )


def chart(request, kana):
    plain = Character.objects.filter(is_plain=True, is_dakuten=False, is_youon=False)
    dakuten = Character.objects.filter(is_dakuten=True, is_youon=False)
    youon = Character.objects.filter(is_youon=True)

    return render_to_response(
        'kana/chart.html',
        {
            'plain': plain,
            'dakuten': dakuten,
            'youon': youon,
            'kana': kana,
        },
        context_instance=RequestContext(request)
    )


def quiz(request, kana, group=None):
    chars = Character.objects.all()

    if group is None:
        chars = chars.filter(is_plain=True)
    elif group == 'dakuten':
        chars = chars.filter(Q(is_dakuten=True) & Q(is_youon=False))
    elif group == 'youon':
        chars = chars.filter(is_youon=True)
    elif group == 'all':
        pass

    return render_to_response(
        'kana/quiz.html',
        {
            'chars': chars,
            'kana': kana,
        },
        context_instance=RequestContext(request)
    )
