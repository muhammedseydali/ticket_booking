from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterCustomerForm

#register a customer

def register_customer(request):
    if request.method == 'POST':
        form = RegisterCustomerForm(request.POST)
        if form.is_valid():
            data  = form.save(commit=False)
            data.is_customer = True
            data.save()
            messages.info(request, 'Your account has been successfully registered, please login to continue...')
            return redirect('login')
        else:
            messages.warning(request, 'something went wrong!!!')
    else:
        form = RegisterCustomerForm()
        context = {'form':form}
        return render(request, 'user_register.html', context)
    
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.info(request, 'Login successfull')
            return redirect('dashboard')
        else:
            messages.warning(request, 'something went wrong!!!')
            return redirect('login')
    else:
        return render(request, 'user/login.html')
    
def logout_user(request):
    logout(request)
    messages.info(request, 'successfully logged out!!!!')
    return redirect('login')