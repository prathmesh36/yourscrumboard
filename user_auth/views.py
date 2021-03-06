from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import logging
# Create your views here.

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,'Your Account has been created, now you can login')
            return redirect('home')
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            form = UserRegisterForm()
            return render(request,'register.html',{'form':form})            

@login_required
def profile(request):
    return render(request, 'profile.html')
