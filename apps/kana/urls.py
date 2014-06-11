from django.conf.urls import patterns, url


urlpatterns = patterns(
    'apps.kana.views',

    url(r'gojuon', 'gojuon', name='gojuon'),
)
