from django.http import HttpResponse
from django.shortcuts import render
from .models import Student

# Create your views here.

def hello(request):
    student_data = Student.students.all()
    print(student_data)
    return render(request,'student/student_list.html',{'student_data':student_data})
