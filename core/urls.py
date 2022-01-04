from django.urls import path
from core.views import Home, AddStudent
 

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("addstudent/", AddStudent.as_view(), name="addstudent")
]
