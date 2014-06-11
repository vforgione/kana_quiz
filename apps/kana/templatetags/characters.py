from django import template

register = template.Library()


@register.filter
def as_romaji(value):
    return value.romaji


@register.filter
def as_hiragana(value):
    return value.hiragana


@register.filter
def as_katakana(value):
    return value.katakana
