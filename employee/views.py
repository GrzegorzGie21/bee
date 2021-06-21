import os

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Document
from .forms import RegisterUserForm, LoginForm


def index(request):
    return render(request, 'home.html')


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    context_object_name = 'employee'


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Employee
    template_name = 'employee_add.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:employee-list')


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'employee_update.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:employee-list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee:employee-list')


class DocumentListView(ListView):
    model = Document
    template_name = 'document_list.html'


class DocumentDetailView(DetailView):
    model = Document
    template_name = 'document_detail.html'
    context_object_name = 'document'


class DocumentCreateView(CreateView):
    model = Document
    template_name = 'document_add.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:document-list')


class DocumentEditView(UpdateView):
    model = Document
    template_name = 'document_update.html'
    fields = '__all__'
    success_url = reverse_lazy('employee:document-list')


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document_delete.html'
    context_object_name = 'document'
    success_url = reverse_lazy('employee:document-list')


class RegisterUserView(View):
    def get(self, request):
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'register_user.html', context)

    def post(self, request):
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            login, password, repeat_password, first_name, last_name, email = form.cleaned_data.values()
            User.objects.create_user(username=login, password=password, first_name=first_name, last_name=last_name,
                                     email=email)
            return redirect('home')
        else:
            messages.add_message(request, messages.ERROR, 'Registration failed!!!')
            context = {'form': form}
            return render(request, 'register_user.html', context)


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username, password = form.cleaned_data.values()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # path = request.GET.get('next')  # automatycznze przekierowanie po logowaniu
                # if path is not None:
                #     return redirect(path)
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, 'Authentication failed!!!')
                context = {'form': form}
                return render(request, 'login.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')