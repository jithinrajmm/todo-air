from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/",UserLogin.as_view(),name = "login"),

    path('register/', RegisterPage.as_view(), name='register'),

    path("logout/",LogoutView.as_view(next_page ='login'),name="logout"),

    path("",Viewtask.as_view(),name="tasks"),

    path("task/<int:pk>/",DetailsTask.as_view(),name="task"),

    path("task-create/",CreateTask.as_view(),name="task-create"),

    path("task-update/<int:pk>/",TaskUpdate.as_view(),name="task-update"),

    path("task-delete/<int:pk>/",TaskDelet.as_view(),name="task-delete")

    ]
