from django.urls import path
from . import views

urlpatterns = [
    path("",views.startPage, name="start-page"),
    path("contacts",views.contactPage,name="contacts-page"),
    path("about",views.aboutPage,name="about-page"),
    path("login",views.loginView,name="login-page"),
    path("signUp",views.signUpView,name="sign-up-page"),
    path("registration",views.registrationPage,name="registration-page"),
]
