from django.shortcuts import render, redirect
from django.http import HttpResponse
from base.models import Tasks

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# this view is used to display the form and rendering respose template
from django.views.generic import FormView
# this form used to create a user
from django.contrib.auth.forms import UserCreationForm
# if the user is completed the registration with out login he can enter to the homw page
from django.contrib.auth import login

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserLoginForm,RegisterUser


class UserLogin(LoginView):
    template_name = "base/login.html"
    form_class = UserLoginForm
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = RegisterUser
    redirect_autheticated_user = True
    success_url = reverse_lazy('login')

    # this is used to store the user details to user database
    # def form_valid(self,form):
    #     user = form.save()
    #     return super().form_valid(form)

    # this is used to store the data to user database and
    # allow the user to automatic login
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    # some times the redirect_authenticated_user is not work
    # then we need to overwrite the get methode

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class Viewtask(LoginRequiredMixin, ListView):
    model = Tasks
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        
        context['count'] = context['tasks'].count()
        context['uncompleteTask'] = context['tasks'].filter(
        complete=False).count()
        
        searchValue = self.request.GET.get('search_value') or ''
        context['searchDefaultvalue'] = searchValue
        
        if searchValue:
            context['tasks'] = context['tasks'].filter(title__icontains= searchValue,user=self.request.user)
            # context['tasks'] = context['tasks'].filter(title__startswith= searchValue,user=self.request.user)
        
            
        return context


class DetailsTask(LoginRequiredMixin, DetailView):
    context_object_name = "task"
    template_name = "base/task.html"

    # default name of html is tasks_detail.html

    model = Tasks


class CreateTask(LoginRequiredMixin, CreateView):
    model = Tasks
    fields = ["title", 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class RegisterUser():
#     def show(self):
#         return HttpResponse('hello jithin raj')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class TaskDelet(LoginRequiredMixin, DeleteView):
    model = Tasks
    context_object_name = "task"
    success_url = reverse_lazy('tasks')


# Create your views here.
