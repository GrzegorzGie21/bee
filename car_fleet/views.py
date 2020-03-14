from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Car, Mileage

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'


class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.odometer = obj.update_odometer()
        obj.save()
        return obj


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


class MileageListView(ListView):
    model = Mileage
    template_name = 'mileage_list.html'


class MileageDetailView(DetailView):
    model = Mileage
    template_name = 'mileage_detail.html'


class MileageCreateView(CreateView):
    model = Mileage
    template_name = 'mileage_add.html'
    fields = ['start_day_odometer', 'end_day_odometer', 'date', 'car']
    success_url = reverse_lazy('mileage-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.distance = self.object.calculate_distance()
        form.save()
        return redirect(self.success_url)


class MileageUpdateView(UpdateView):
    model = Mileage
    fields = ['start_day_odometer', 'end_day_odometer', 'date', 'car']
    template_name = 'mileage_update.html'
    success_url = reverse_lazy('mileage-list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.distance = self.object.calculate_distance()
        form.save()
        return redirect(self.success_url)


class MileageDeleteView(DeleteView):
    model = Mileage
    template_name = 'mileage_delete.html'
    success_url = reverse_lazy('mileage-list')
