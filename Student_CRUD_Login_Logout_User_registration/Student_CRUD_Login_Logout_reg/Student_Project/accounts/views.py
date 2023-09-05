from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
# Create your views here.

def login(request):
    if request.method == "POST":
        user_name = request.POST['username']
        pwd1 = request.POST['password']
        user = auth.authenticate(request,username=user_name,password=pwd1)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.error(request,"Login Failed !!")
            return redirect("login")
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect("login")

def register(request):
    if request.method == "POST":
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        user_name = request.POST['username']
        email = request.POST['email']
        pwd1 = request.POST['password1']
        pwd2 = request.POST['password2']

        if (pwd1 == pwd2):
            if(User.objects.filter(username=user_name)):
                messages.success(request,"Username Already Exists")
                return render(request, 'register.html')
            elif(User.objects.filter(email=email)):
                messages.success(request, "Email Taken")
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=user_name, email=email, password=pwd1, first_name=first_name,
                                                last_name=last_name)
                user.save()
                return redirect("login")
        else:
            messages.success(request, 'Password does not match')
            return render(request, 'register.html')


        return render(request, 'login.html', {})
    else:
        return render(request,'register.html',{})

