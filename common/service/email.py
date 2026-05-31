from django.core.mail import send_mail, EmailMessage
from config.settings import BASE_DIR
import os

def send_simple_email():
    send_mail(
        subject="Django email sinov",
        message="Bu test sinovi",
        from_email="oybekjon763@gmail.com",
        recipient_list=["subwayrush841@gmail.com", "davronbekn202@gmail.com"],
        fail_silently=False
    )


def send_email_with_attachment():
    file_path = os.path.join(BASE_DIR, 'common/service/file.txt')

    if not os.path.exists(file_path):
        print("Fayl topilmadi!")

        return
    email = EmailMessage(
        subject="Fayl bilan email",
        body="Mana sizga biriktirilgan fayl.",
        from_email="oybekjon763@gmail.com",
        to=["subwayrush841@gmail.com"],
    )
    with open(file_path, "rb") as f:
        email.attach("file.txt", f.read(), "application/pdf")
    email.send()