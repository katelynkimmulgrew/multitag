from django.conf.urls import url

from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^page/(?P<page_number>[0-9]+)/$', views.result, name = 'result'),
        ]
