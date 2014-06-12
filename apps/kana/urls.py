from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.kana.views',

    url(r'gojuon(?:/(?P<kana>hiragana|katakana))?', 'gojuon', name='gojuon'),
)
