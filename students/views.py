from django.shortcuts import render,redirect, get_object_or_404
from .models import Students
from .forms import StudentsForm
# Create your views here.

def student_list(request):
    students = Students.objects.all()
    return render (request,'students/student_list.html',{'students':students})

def add_student(request):
    form=StudentsForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_forms.html',{'form':form})

def update_student(request,id):
    student=get_object_or_404(Students,id=id)
    form= StudentsForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect('student_list')
    return render(request,'students/student_forms.html',{'form':form})

def delete_student(request,id):
    student=get_object_or_404(Students,id=id)
    student.delete()
    return render('student_list') 