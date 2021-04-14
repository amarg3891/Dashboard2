from django.shortcuts import render,redirect
from django.contrib import messages # for print the message
from django.contrib.auth.models import User, auth
from .forms import UserRegistration

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')

def show_data(request):
    if request.method == 'POST':
        fm = UserRegistration(request.POST)
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        rpassword = request.POST['rpassword']

        if password == rpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')


            else:
                user = User.objects.create_user(username=username, password = password,first_name = first_name, last_name = last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'password not matching..')
            return redirect('register')
        return redirect('/')
    else:
        fm = UserRegistration()
    return render(request,'register.html',{'form':fm})
