from django.shortcuts import render
from .forms import RegistrationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Handle registration logic here
            return render(request, "success.html")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})