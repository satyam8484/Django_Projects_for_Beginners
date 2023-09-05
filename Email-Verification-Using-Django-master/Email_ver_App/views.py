from django.shortcuts import render, redirect
from .models import verification_model
from django.core.mail import send_mail
from django.contrib import messages
import random


# Create your views here.

def verify(request):
    return render(request, 'verify.html')


def email_verification_code(request):
    if "get_code_val" in request.POST:
        email = request.POST['email']

        l1 = [str(i) for i in range(1, 9)]
        l1 = l1 + [chr(i) for i in range(65, 90)]
        random.shuffle(l1)
        verify_code = "".join(l1)

        flag = verification_model.objects.filter(email=email).exists()
        if flag:
            verification_model.objects.filter(email=email).update(verification_code=verify_code)
        else:
            v1 = verification_model(email=email, verification_code=verify_code)
            v1.save()

        msg = """Dear,
            Please Copy Below Verification Code For Email Verification     
        Your Verification code is {}
        
        Thanks and Regards,
        Email App
        """.format(verify_code)

        try:
            send_mail(
                'Regarding Verification Mail',
                msg,
                'Your Gmail id of Setting.py',
                [email],
                fail_silently=False,
            )
        except Exception as e:
            messages.error(request, 'Something Went Wrong')
            return redirect('verify')

    elif "verify_val" in request.POST:
        email = request.POST['email']
        verification_code = request.POST['verification_code']

        if verification_code is "":
            messages.error(request, 'Please Enter Verification Code')
            return redirect('verify')

        data = verification_model.objects.filter(email=email)

        if (data[0].verification_code == verification_code):
            info_msg=""
            return render(request, 'another.html', {'msg': info_msg})
        else:
            messages.error(request, 'Verification Code Doesn\'t match')
            return redirect('verify')

    return redirect('verify')


def send_Gmail(request):

    email=request.POST['email']
    password = request.POST['password']

    send_mail(
        subject='Welcome To Mail Application',
        message='Dear,\nyou are successfully Register For our Application\nNow you can Enjoy Our service\nThanks & Regards,\nsatyam',
        from_email='pawarsatyam269@gmail.com',
        recipient_list=[email, ],
        auth_user=email,
        auth_password=password,
        fail_silently=False,)

    return render(request,'another.html',{'msg':'Please Check Your Mail'})


