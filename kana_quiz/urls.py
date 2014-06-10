from django.conf.urls import patterns, include, url
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns(
    '',

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # kana app
    url(r'^', include('apps.kana.urls', namespace='kana')),
)
