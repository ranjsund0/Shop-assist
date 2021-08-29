from django.urls import path     
from . import views

urlpatterns = [
    # renders
    path('', views.index),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', views.logout),
    path('loginReg/', views.loginReg),
    path('description/', views.description)
    

    # redirects

]