from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path('sign_in', views.SignInView.as_view(), name='sign_in'),
    path('sign_up', views.ProflieCreateView.as_view(), name='sign_up'),
    path('password_reset', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_forgot', views.PasswordForgotView.as_view(), name='password_forgot'),
    path('profile', views.ProfileUpdateView.as_view(), name='profile'),
]
