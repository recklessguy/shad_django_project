from django.contrib import auth
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
from .views import PasswordsChangeView
urlpatterns = [
    path("signup/", views.signupPage, name='signup'), 
    path("login/", views.loginPage, name='login'), 
    path("logout/", views.logoutUser, name='logout'),
    path("change_password", PasswordsChangeView.as_view(template_name='registration/change-password.html')),
]
