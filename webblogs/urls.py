from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<page>[0-9]+)/page$', views.index_page, name='index_page'),
    url(r'^(?P<post_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new_post/$', views.new_post, name="new_post"),
    url(r'^(?P<post_id>[0-9]+)/edit/$', views.edit, name="edit"),
    url(r'^(?P<post_id>[0-9]+)/delete/$', views.delete, name="delete"),
]