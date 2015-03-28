from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url('countryform', views.countryform, name='countryform'),
    url('countryanalysis', views.countryanalysis, name='countryanalysis'),
    url('twohashtagfrecuencyform', views.twohashtagfrecuencyform, name='countryform'),
    url('twohashtagfrecuencyanalisis', views.twohashtagfrecuencyanalisis, name='twohashtagfrecuencyanalisis'),
    url('countrytwohashtagform', views.countrytwohashtagform, name='countrytwohashtagform'),
    url('countrytwohashtaganalisis', views.countrytwohashtaganalisis, name='countrytwohashtaganalisis'),

    url('twokeywordintwitterandredditform', views.twokeywordintwitterandredditform, name='twokeywordintwitterandredditform'),
    url('twokeywordintwitterandredditanalisis', views.twokeywordintwitterandredditanalisis, name='twokeywordintwitterandredditanalisis'),

    url('keywordintwitterandredditform', views.keywordintwitterandredditform, name='keywordintwitterandredditform'),
    url('keywordintwitterandredditanalisis', views.keywordintwitterandredditanalisis, name='keywordintwitterandredditanalisis'),


    url(r'^$', views.index, name='index'),

)
