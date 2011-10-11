from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('',
        url(r'^fan/?$', 'droiduino.views.fan'),
)
