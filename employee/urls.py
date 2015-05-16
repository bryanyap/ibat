from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^get/(?P<employee_id>\d+)$', views.employee),
    url(r'^all/$', views.employee),
]
