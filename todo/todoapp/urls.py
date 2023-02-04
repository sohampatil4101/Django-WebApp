from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.home, name="home" ),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('login', views.loginuser, name="loginuser"),
    path('todo', views.todo, name="todo"),
    path('register', views.register, name="register"),
    path('todolist', views.todolist, name="todolist"),
    path('todolist2', views.todolist2, name="todolist2"),
    path('delete/<str:task>', views.delete, name="delete")
]
