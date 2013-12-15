from django.conf.urls import patterns, include, url

from django.contrib import admin
#from game import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adventuregame.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'adventuregame.views.home', name='home'),
    #url(r'^blog/', views.index, name='index'),
    url(r'^blog/', include('game.urls', namespace="game")),
)
