from django.shortcuts import render

from django.urls import reverse_lazy
from .models import Customer,CustomerAddress
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerAddView(CreateView):
    model = Customer
    template_name = 'customer_add.html'
    fields = '__all__'
    success_url = reverse_lazy('customer-list')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('update-customer', args=[self.object.pk])


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer-list')


class CustomerAddressListView(ListView):
    model = CustomerAddress
    template_name = 'customer_address_list.html'


class CustomerAddressAddView(CreateView):
    model = CustomerAddress
    template_name = 'customer_address_add.html'
    fields = '__all__'
    success_url = reverse_lazy('customer-addresses')


class CustomerAddressUpdateView(UpdateView):
    model = CustomerAddress
    template_name = 'customer_address_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('update-address', args=[self.object.pk])


class CustomerAddressDeleteView(DeleteView):
    model = CustomerAddress
    template_name = 'customer_address_delete.html'
    success_url = reverse_lazy('customer-addresses')