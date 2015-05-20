from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /surveys/
    url(r'^$', views.index, name='index'),
    # ex: /surveys/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /surveys/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /surveys/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]