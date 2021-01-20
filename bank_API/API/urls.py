from django.urls import path
from . import views

urlpatterns = [
    path("", views.simple_api),
    path("data/", views.home),
    path('api/', views.apiOverview),
    path('task-list/', views.banklist),
]