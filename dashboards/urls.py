from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^matches/$', views.matches, name='matches'),
    url(r'^diagnosis/$', views.diagnosis, name='diagnosis'),
    url(r'^scheduler/$', views.scheduler, name='scheduler'),
]