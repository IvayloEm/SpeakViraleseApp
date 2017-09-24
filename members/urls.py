from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^writer-view/', views.writer_view, name="writer-view"),
]