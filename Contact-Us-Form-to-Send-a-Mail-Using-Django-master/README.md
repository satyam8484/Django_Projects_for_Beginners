# Contact-Us-Form-to-Send-a-Mail-Using-Django
  Here i have created a Contact us Form which will store user Information in Database 
and Send a promotional mail to user using Django

# requirements
python3.6 >=


# Installation 
pip install django

# Run
then do some changes in setting.py and views.py

- in setting.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'

EMAIL_PORT = '587'

EMAIL_HOST_USER = 'Your mail id'        # Change This 

EMAIL_HOST_PASSWORD = 'your Password'   # Change This

EMAIL_USE_TLS = True

EMAIL_USE_SSL = False


- in Views.py

send_mail(
            'Thank you For Cotacting Us',
            msg,  # Message
            'Your mail id',  
            [tomailadd],
            fail_silently=False,
        ) # Change This

- run following command
python manage.py runserver









