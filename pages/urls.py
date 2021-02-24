from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'), # Root path (home page) could be /
    path('about', views.about, name='about'),
]