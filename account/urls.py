from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views

app_name = 'account'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

#   forgot password
    path('forgot_password/', views.forgot_password, name='forgot'),
    path("verify/", views.verify_otp, name="verify_otp"),
    path("reset/", views.reset_password, name="reset_password"),
]
