"""Helloword URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
 
from . import view,search,search2,login

 
urlpatterns = [
    url(r'^$', view.hello),
    url(r'^search-form$', search.search_form),
    url(r'^search$', search.search),
    url(r'^search-post$', search2.search_post),
    url(r'^search-test$', search.getkc),
    url(r'^login$', login.index),
    url(r'^test$', login.test),
    url(r'^login-post$', login.login_post),
    url(r'^webSet$', search.getkc),
    url(r'^recommend$', search.recommend),
    url(r'^login.html$', login.index),
    url(r'^findInfo$', search.test),
]
