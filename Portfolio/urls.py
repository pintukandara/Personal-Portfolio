from django.urls import path

from Portfolio import views

urlpatterns =[
    path("",views.intro,name= "home"),
    path("message-me/", views.connect, name = "message-me"),



]