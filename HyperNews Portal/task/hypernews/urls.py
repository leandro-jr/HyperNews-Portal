"""hypernews URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from django.views import View
from news.views import NewsView, LinkView
from django.shortcuts import redirect


class ComingSoon(View):
    def get(self, request, *args, **kwargs):
        # html = '<a target="_blank" target="_blank" href="/news/">Coming soon</a>'
        # return HttpResponse(html)
        return redirect('/news/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ComingSoon.as_view()),
    path("news/", NewsView.as_view()),
    path("news/create/", include('news.urls')),
    re_path("news/(?P<link>[^/]*)/?/", LinkView.as_view()),
    path("news/create/", include('news.urls')),
]
