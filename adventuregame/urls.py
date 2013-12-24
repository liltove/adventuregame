from django.conf.urls import patterns, include, url

from django.contrib import admin
#from game import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adventuregame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^game/', include('game.urls', namespace="game")),
)
