from django.shortcuts import render
from core.models import Student
from django.contrib import messages

 

# Create your Viewss here.

def home(request):
    student = Student.objects.all()
    return render(request, 'home.html',{'students':student})
       
    
def addstudent(request):
    
    if  request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        addstu = Student(name=name, email=email, address=address)
        addstu.save()
        messages.success(request, "your From Has been submited")
    return render(request, 'addstudent.html')

