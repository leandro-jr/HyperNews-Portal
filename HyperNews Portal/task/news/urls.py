from django.urls import path
from .views import CreateNews

urlpatterns = [
    path('', CreateNews.as_view()),
]