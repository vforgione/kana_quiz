from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.kana.views',

    url(r'^$', 'home', name='home'),
    url(r'^chart/(?P<kana>hiragana|katakana)', 'chart', name='chart'),
    url(r'^quiz/(?P<kana>hiragana|katakana)$', 'quiz', name='quiz'),
    url(r'^quiz/(?P<kana>hiragana|katakana)/(?P<group>dakuten|youon|all)', 'quiz', name='quiz'),
)
