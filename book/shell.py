from django.conf import settings
from django.core.mail import send_mail

send_mail(
     subject='A cool subject',
     message='A stunning message',
     from_email=settings.EMAIL_HOST_USER,
    recipient_list=(['vinay.chavan590@gmail.com']))

#exec(open('D:\Vinay_Workbench\B6_Library\book\shell.py').read())

