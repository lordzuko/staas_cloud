from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'cloud' 
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^upload/$', views.upload, name='upload'),
]
