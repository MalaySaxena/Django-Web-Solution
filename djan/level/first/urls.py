from django.urls import path, include
from . import views

urlpatterns = [
    path('h/', views.index, name='index'),

]
