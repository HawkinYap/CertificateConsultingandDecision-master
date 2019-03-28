from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.cert_list, name='cert_list'),
    url(r'(?P<result_id>\d+)/$', views.cert_result, name="cert_result"),
    url(r'search/$', views.search, name="search")
]