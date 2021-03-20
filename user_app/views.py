from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "headings": ["ID", "Name", "Email", "Age"],
        "all_users": User.objects.all(),
    }
    return render(request, 'users.html', context)

def process_form(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email_address=request.POST['email_address'], age=request.POST['age'])
    return redirect('/')