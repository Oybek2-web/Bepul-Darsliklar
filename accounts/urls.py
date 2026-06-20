# from django.contrib.auth import views as auth_views
# from django.urls import path, reverse_lazy, include
# from . import views
#
# app_name = 'accounts'
#
# urlpatterns = [
#     path('accounts', include('allauth.urls')),
#     path('register/', views.register, name='register'),
#     path('login_/', views.login_user, name='login'),
#     path('logout/', views.logout_user, name='logout'),
#
# #   forgot password
#     path('forgot_password/', views.forgot_password, name='forgot'),
#     path("verify/", views.verify_otp, name="verify_otp"),
#     path("reset/", views.reset_password, name="reset_password"),
# ]

from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', include('allauth.urls')),  # ← 'accounts' emas, '' (bo'sh) qiling
    path('register/', views.register, name='register'),
    path('login_', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('forgot_password/', views.forgot_password, name='forgot'),
    path("verify/", views.verify_otp, name="verify_otp"),
    path("reset/", views.reset_password, name="reset_password"),
]
