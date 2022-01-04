from django.shortcuts import render
from django.views import View
from core.models import Student
from core.forms import StudentForm
from django.views.generic.edit import FormView

# Create your Viewss here.

class Home(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, 'home.html', {'students':student})
    
class AddStudent(View):
    def get(self, request):
        return render(request, 'addstudent.html')