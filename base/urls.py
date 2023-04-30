from django.urls import path
from base import views

urlpatterns = [
    path('', views.index2, name='index2')
]
