from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def brands(request):
    return render(request, 'brands/brands.html' )
def memory(request):
   return HttpResponse("This is memory page")   
