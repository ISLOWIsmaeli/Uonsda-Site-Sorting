from django.urls import path
from . import views

urlpatterns = [
    path("",views.startPage, name="start-page"),
    path("contacts",views.contactPage,name="contacts-page"),
    path("about",views.aboutPage,name="about-page"),
    path("login",views.loginView,name="login-page"),    
    path("logout",views.logoutView,name="logout-page"),    
    path("signUp",views.signUpView,name="sign-up-page"),
    path("registration",views.registrationPage,name="registration-page"),
    path("upload_excel",views.uploadExcelView,name="upload-excel-page"), #to reorganize into staff
    path("random_groups",views.randomGroups,name="random-groups-page"),# to relook the algorithm
]
