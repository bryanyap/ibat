from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^get/(?P<vendor_id>\d+)$', views.vendor),
    url(r'^all/$', views.vendors),
]
