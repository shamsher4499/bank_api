from django.urls import path
from . import views

urlpatterns = [
    path("", views.simple_api),
    path("data/", views.home),
    # path('bank-list/', views.banklist),
    path('bank-data/', views.BankList.as_view()),
    path('bank/', views.index),

]