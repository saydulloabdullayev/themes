from django.urls import path
from . import views

urlpatterns = [
    path('', views.theme_list, name='theme_list'),
]
