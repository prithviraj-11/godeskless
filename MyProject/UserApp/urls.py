from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^user$',views.userApi),
    url(r'^user/([0-9]+)$',views.userApi),
]