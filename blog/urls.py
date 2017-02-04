from django.conf.urls import urls
from . import views

urls patterns = [
	url(r'^$', views.post_list, name='post_list')
]