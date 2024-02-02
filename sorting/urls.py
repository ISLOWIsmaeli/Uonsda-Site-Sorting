from django.urls import path
from . import views

urlpatterns = [
    path("",views.startpage, name="start_page"),
]
