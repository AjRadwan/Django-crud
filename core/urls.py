from django.urls import path
from core import views
    

urlpatterns = [
    path('', views.home, name="home"),
    path('addstudent', views.addstudent, name="addstudent"),
    path('<int:id>', views.delete, name="delete"),
    path('edit/<int:id>', views.edit, name="edit")
]
