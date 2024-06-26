from django.urls import path
from . import views

urlpatterns = [
    path("",views.startPage, name="start_page"),
    path("contacts",views.contactPage,name="contacts_page"),
    path("about",views.aboutPage,name="about_page"),
    path("login",views.loginView,name="login_page"),
    path("signUp",views.signUpView,name="sign_up_page"),
]
