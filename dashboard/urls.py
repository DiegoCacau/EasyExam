from django.urls import re_path
from .views import *

urlpatterns = [
    re_path(r'^$', IndexView.as_view(), name='index'),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^configuracao/$', ConfigurationView.as_view(), name='configuration'),
]
