from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import *


def gojuon(request):
    chars = Character.objects.all()
    return render_to_response(
        'kana/gojuon.html',
        {
            'chars': chars,
        },
        context_instance=RequestContext(request)
    )
