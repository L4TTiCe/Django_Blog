from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='blog-landing'),
    path('about/', views.about, name='blog-about'),
]