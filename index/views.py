from django.http import HttpResponse
from django.shortcuts import render
from .models import contactform
from django.template import RequestContext

def home(request):
    return render(request, 'index.html' )

def about(request):
    return render(request, 'about.html' ) 

def brands(request):
    return render(request, 'brands.html' )    

def contacts(request):
    if request .method == 'POST' :
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contactformdata = contactform(name = name, email = email, subject = subject, message = message)
        contactformdata.save()
    return render(request, 'contacts.html')
       