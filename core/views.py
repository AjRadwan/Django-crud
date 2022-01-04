from django.shortcuts import render
from django.views import View
from core.models import Student
# Create your Viewss here.

class Home(View):
    def get(self, request):
        student = Student.objects.all()
        return render(request, 'home.html', {'students':student})
    
 