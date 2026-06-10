from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from account.forms import UserRegisterForm
from django.contrib.auth.models import User
from account.utils import login_required, send_reset_password_email
import random


# REGISTER
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password1')
            )
            # login(request, user)
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('fanlar:fanlar_list')
        else:
            return render(request, 'account/register.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, 'account/register.html', {'form': form})

# LOGIN
def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next') or request.POST.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('fanlar:fanlar_list')
    else:
        form = AuthenticationForm()
    return render(request,'account/login.html',{'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('account:login')


# def verify_otp(request):
#     if request.method == "POST":
#         user_code = request.POST.get("code")
#         real_code = request.session.get('reset_code')
#
#         if user_code == real_code:
#             return redirect('account:reset_password')
#         else:
#             return render(request, "account/password_reset_done.html", {"error": "Wrong OTP"})
#     return render(request, "registration/password_reset_done.html")

def verify_otp(request):
    if request.method == "POST":
        user_code = request.POST.get("code")
        real_code = request.session.get('reset_code')

        # Ikkalasini ham string qilib taqqoslaymiz
        if str(user_code) == str(real_code):
            return redirect('account:reset_password')
        else:
            return render(request, "account/verify_otp.html", {"error": "❌ Noto'g'ri kod! Qaytadan urinib ko'ring."})

    # GET so'rovda yangi shablonni ko'rsatamiz
    return render(request, "account/verify_otp.html")


def reset_password(request):
    if request.method == "POST":
        email = request.session.get('reset_email')
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not email:
            return redirect('account:forgot')

        if password1 != password2:
            return render(request, "registration/reset_password.html", {
                "error": "❌ Parollar mos kelmadi!"
            })

        if len(password1) < 6:
            return render(request, "registration/reset_password.html", {
                "error": "❌ Parol kamida 6 ta belgidan iborat bo'lishi kerak!"
            })

        # ✅ BU YERDA O'ZGARTIRISH KIRITILDI
        user = User.objects.filter(email=email).first()

        if not user:
            return render(request, "registration/reset_password.html", {
                "error": "Bu email bilan foydalanuvchi topilmadi."
            })

        user.set_password(password1)
        user.save()

        # Sessiyadan kod va emailni tozalaymiz
        if 'reset_code' in request.session:
            del request.session['reset_code']
        if 'reset_email' in request.session:
            del request.session['reset_email']

        return redirect('account:login')

    return render(request, "registration/reset_password.html")


from .forms import ForgotPasswordForm

def forgot_password(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not User.objects.filter(email=email).exists():
            return render(
                request,
                "registration/password_reset_form.html",
                {"error": "Bu email topilmadi"}
            )

        code = random.randint(100000, 999999)

        request.session["reset_email"] = email
        request.session["reset_code"] = code

        send_reset_password_email(email, code)

        return redirect("account:verify_otp")

    return render(request, "registration/password_reset_form.html")