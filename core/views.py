from django.shortcuts import render, redirect
from core.models import Student
from django.contrib import messages
from core.forms import StudentForm
# Create your Viewss here.

def home(request):
    student = Student.objects.all()
    return render(request, 'home.html',{'students':student})
       
    
def addstudent(request):
    if request.method == 'POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
           name = fm.cleaned_data['name']
           email = fm.cleaned_data['email']
           address = fm.cleaned_data['address']
           student = Student(name=name, email=email, address=address)
           student.save()
           messages.success(request, "Your From has been submitted")
           fm = StudentForm()
    else:
        fm = StudentForm()
    return render(request, 'addstudent.html', {'form':fm})


def edit(request, id):
    if request.method == 'POST':
        stuId = Student.objects.get(id=id)  
        fm = StudentForm(request.POST, instance=stuId)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Your From has been Updated")
            
    else:
        stuId = Student.objects.get(id=id)  
        fm = StudentForm(instance=stuId)
    return render(request, 'edit.html', {'form': fm})
    
    


def delete(request, id):
    student = Student.objects.get(id=id)  
    student.delete()  
    messages.warning(request, "Your list has been Deleted")
    return redirect('home')