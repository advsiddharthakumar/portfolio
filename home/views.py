from django.shortcuts import render
from datetime import datetime
from home.models import Contact

def index(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method =="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact= Contact(name=name, email=email, phone=phone, subject=subject, message=message, date=datetime.today())
        contact.save()

    return render(request,'contact.html')
