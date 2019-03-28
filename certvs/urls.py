from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'getvs/$', views.getvs, name="getvs")
]