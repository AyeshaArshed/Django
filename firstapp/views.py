from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now()
    student = {
        'name': 'ayesha',
        'age': 23
    }
    data = {
        'date': date,
        'student':student,
    }
    return render(request,'firstapp/home.html',data)

def about_us(request):
    name_using_in_form = request.GET.get('name')
    isActive = False
    about_detail = {
        'email': 'ayesha@gmail.com',
        'name': 'Ayesha',
        'isActive': isActive,
        'name_using_in_form':name_using_in_form
    }
    return render(request,'firstapp/about.html',about_detail)

def services(request):
    return render(request,'firstapp/services.html')
