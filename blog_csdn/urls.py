"""blog_csdn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from backend import views
from web import views as view_web
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user_register.html$', views.user_register),
    url(r'^user_login.html$', views.user_login),
    url(r'^check_code.html$', views.check_code),
    url(r'^index.html$', view_web.index),
    url(r'^admin_index.html$', views.admin_index),
    url(r'^user_logout.html$', views.logout),
    url(r'^user_register_success.html$', views.user_register_success),

]
