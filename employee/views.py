from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Employee, Document


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
    success_url = reverse_lazy('employee-list')


class EmployeeEditView(UpdateView):
    model = Employee
    template_name = 'employee_update.html'
    fields = '__all__'
    success_url = reverse_lazy('employee-list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    context_object_name = 'employee'
    success_url = reverse_lazy('employee-list')


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
    success_url = reverse_lazy('document-list')


class DocumentEditView(UpdateView):
    model = Document
    template_name = 'document_update.html'
    fields = '__all__'
    success_url = reverse_lazy('document-list')


class DocumentDeleteView(DeleteView):
    model = Document
    template_name = 'document_delete.html'
    context_object_name = 'document'
    success_url = reverse_lazy('document-list')

