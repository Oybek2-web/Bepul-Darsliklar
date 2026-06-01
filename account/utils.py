from django.shortcuts import redirect
from django.template.loader import render_to_string


import threading
from django.core.mail import send_mail
from django.conf import settings

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return func(request, *args, **kwargs)
        else:
            return redirect('account:login')
    return wrapper

from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings


def send_reset_password_email(email, code):

    html_message = render_to_string(
        'registration/password_reset_email.html',
        {
            'code': code
        }
    )

    plain_message = f"Your OTP code is: {code}"

    msg = EmailMultiAlternatives(
        subject="Password Reset OTP",
        body=plain_message,
        from_email=settings.EMAIL_HOST_USER,
        to=['subwayrush841@gmail.com'],
    )

    msg.attach_alternative(html_message, "text/html")
    msg.send(fail_silently=False)






























































# def send_email_thread(subject, message, recipient_email):
#     """Email yuborishni alohida threadda bajaradi.
#     Sahifa "muzlab" qolmaydi — foydalanuvchi kutmaydi."""
#
#     def _send():
#         send_mail(
#             subject=subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[recipient_email],
#             fail_silently=False,
#         )
#
#     thread = threading.Thread(target=_send)
#     thread.daemon = True
#     thread.start()