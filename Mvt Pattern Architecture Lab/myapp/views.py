from django.shortcuts import render
from .models import Form 

# Create your views here.

def form(request):
    return render(request,'form.html')