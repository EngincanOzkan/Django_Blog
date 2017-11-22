from django.conf.urls import url
from .views import post_index,post_detail,post_create,post_update,post_delete

app_name = 'post'

urlpatterns = [
    url(r'^index/$', post_index, name="index"),
    url(r'^create/$', post_create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name="detail"),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name="update"),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name="delete"),
]
