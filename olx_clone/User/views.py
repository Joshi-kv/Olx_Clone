from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages,auth
# Create your views here.
def signup(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
              messages.error(request,'Username already exists')
              return redirect('User:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email alredy taken")
                return redirect('User:signup')
            else:  
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('User:login')
        else :
            messages.error(request,'Password not matching')
            return redirect('User:signup')
    return render(request,'signup.html')
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('Home:home_page')
        else:
            messages.error(request,'Invalid username or password')
            return redirect('User:login')
    return render(request,'login.html')