from django.urls import path
from core import views
    

urlpatterns = [
    path('', views.home, name="home"),
    path('addstudent', views.addstudent, name="addstudent"),
    path('basic', views.basic, name="basic")
]
