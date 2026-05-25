from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

# 1) Email kiritish sahifasi
    path('forgot-password/',
         auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html',
             success_url=reverse_lazy('account:password_reset_done')
         ), name='password_reset'),

    # 2) "Email yuborildi" xabari
    path('forgot-password/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='registration/password_reset_done.html'
         ), name='password_reset_done'),

    # 3) Yangi parol kiritish (email'dagi link orqali)
    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), name='password_reset_confirm'),

    # 4) Muvaffaqiyat sahifasi
    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ), name='password_reset_complete')
]
