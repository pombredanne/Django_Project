from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^login/$', views.log_in, name='login'),
    url(r'^activate/$',
        views.activate_user_account, name='activate_user_account'),
]
