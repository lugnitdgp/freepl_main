"""freepl_main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


admin.site.site_header = 'FREEPL | Aavishkar 2.0'
admin.site.site_title = 'FREEPL | Aavishkar 2.0'

app_name='freepl'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.urls')),
    url('', include(('social.apps.django_app.urls','social'), namespace='social')),
    url('', include(('django.contrib.auth.urls','auth'), namespace='auth')),
    url(r'^api-auth/', include('rest_framework.urls')),
]
