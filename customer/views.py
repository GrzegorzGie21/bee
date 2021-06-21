from django.shortcuts import render

from django.urls import reverse_lazy
from .models import Customer, CustomerAddress
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'


class CustomerAddView(CreateView):
    model = Customer
    template_name = 'customer_add.html'
    fields = '__all__'
    success_url = reverse_lazy('customer:customer-list')


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('customer:customer-list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_delete.html'
    success_url = reverse_lazy('customer:customer-list')


class CustomerAddressListView(ListView):
    model = CustomerAddress
    template_name = 'customer_address_list.html'


class CustomerAddressDetailView(DetailView):
    model = CustomerAddress
    template_name = 'customer_address_detail.html'


class CustomerAddressAddView(CreateView):
    model = CustomerAddress
    template_name = 'customer_address_add.html'
    fields = '__all__'
    success_url = reverse_lazy('customer:customer-addresses')


class CustomerAddressUpdateView(UpdateView):
    model = CustomerAddress
    template_name = 'customer_address_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('customer:customer-addresses')


class CustomerAddressDeleteView(DeleteView):
    model = CustomerAddress
    template_name = 'customer_address_delete.html'
    success_url = reverse_lazy('customer:customer-addresses')
