from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Extra imports
from django.contrib.auth import authenticate, login, logout
from .forms import UserFrom, UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

@login_required
def other(request):
    return render(request,'basic_app/other.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

    
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserFrom(data=request.POST)
        user_profile = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile.is_valid():

            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = user_profile.save(commit=False)

            profile.user = user

            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True

        else:
            print(user_form.errors,user_profile.errors)

    else:
        user_form = UserFrom()
        user_profile = UserProfileInfoForm()

    return render(request,'basic_app/registration.html',
                         {'user_form':user_form,
                          'user_profile':user_profile,
                          'registered':registered})



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # authenticate the user
        user = authenticate(username=username,password=password)

        # if we have a user
        if user:
        # check if user is active
            if user.is_active:
                login(request,user)

                # send user back to homepage
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("user is not active")

        else:
            return HttpResponse("not a user")


    else:
        return render(request,'basic_app/login.html')
