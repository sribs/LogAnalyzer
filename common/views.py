from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def  home(request):
    return render(request,'common/home.html',context={'title':'Linux Log Analyzer'})

def register(request):
    if request.method=='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account Created for {username}!')
            return redirect('common-login')
    else:
        form = UserRegisterForm()
    return render(request,'common/register.html',{'form':form}) 

def login(request):
    return render(request,'common/login_register.html',context={'login_form_type':True})