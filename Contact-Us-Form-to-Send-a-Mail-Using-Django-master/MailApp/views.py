from django.shortcuts import render
from .models import Contact_usr
from django.core.mail import send_mail


# Create your views here.

def contactform(request):
    return render(request, 'contactform.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        number = request.POST['number']
        email = request.POST['email']
        message = request.POST['message']

        cnt_obj = Contact_usr(name=name, phone_number=number, email=email, message=message)
        cnt_obj.save()

        tomailadd = email
        msg = f'''Dear {name},

	Welcome to coding Disco, Thank you for taking interest.

Please feel free to reach out us for Projects And Online Cources.

For More Such type Content 
Please follow | Like | Comment | Share 
@coding_disco

Thanks & Regards,
Satyam
'''
        send_mail(
            'Thank you For Cotacting Us',  # Subject
            msg,  # Message
            'Your GMail id that u specify in setting.py',  # From
            [tomailadd],  # To
            fail_silently=False,
        )

        print('Record Inserted Successfully')
        return render(request, 'contactform.html', {'msg': 'Your Message has been recorded Successfully'})
