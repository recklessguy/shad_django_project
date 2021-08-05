from django.shortcuts import render, redirect
from django.contrib import messages
from django.http.response import HttpResponse 
from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.urls.base import reverse, reverse_lazy
from .forms import CreateUserForm
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required

def signupPage(request):
    if request.user.is_authenticated:
        return redirect('add_writings')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                
                messages.success(request,'Account succesfully created for ' + user)
                return redirect('login')


        context = {'form':form}
        return render(request, 'registration/signup.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('add_writings')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('add_writings')
            
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'registration/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')

    