"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^list/', include('list.urls', namespace='list', app_name='list')),
    url(r'^account/', include('account.urls', namespace='account', app_name='account')),
    url(r'^blog/', include("blog.urls", namespace="blog", app_name="blog")),
    url(r'^article/', include('article.urls', namespace='article', app_name='article')),
    url(r'^image/', include('image.urls', namespace='image', app_name='image')),
    url(r'^contract/', include('contract.urls', namespace='contract', app_name='contract')),
    url(r'^certvs/', include('certvs.urls', namespace='certvs', app_name='certvs')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)