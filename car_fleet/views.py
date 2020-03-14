from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'


class CarCreateView(CreateView):
    model = Car
    template_name = 'car_add.html'
    fields = '__all__'
    success_url = reverse_lazy('car-list')


class CarUpdateView(UpdateView):
    model = Car
    fields = '__all__'
    template_name = 'car_update.html'
    success_url = reverse_lazy('car-list')


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('car-list')
