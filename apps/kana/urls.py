from django.conf.urls import patterns, include, url


urlpatterns = patterns(
    'apps.kana.views',

    url(r'^gojuon', 'gojuon', name='gojuon'),
)
