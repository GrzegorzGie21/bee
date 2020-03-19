from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import edit

from .models import Order, OrderProducts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddProductToOrderForm


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_products'] = OrderProducts.objects.filter(order=self.object)
        return context


class OrderAddView(CreateView):
    model = Order
    template_name = 'order_add.html'
    fields = ['date', 'user', 'customer']

    def form_valid(self, form):
        object = form.save(commit=False)
        object.number = object.calculate_number()
        object.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('order:order-detail', args=[self.object.pk])


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    fields = ['number', 'date', 'user', 'customer']

    def get_success_url(self):
        return reverse_lazy('order:order-detail', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_products'] = OrderProducts.objects.filter(order=self.object)
        context['form2'] = AddProductToOrderForm(initial={'order': self.object})
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.POST.get('delete_product') == 'delete':
            order_products = OrderProducts.objects.filter(order=self.object).values('id')
            for order_id in order_products:
                for value in order_id.values():
                    if request.POST.get('product_id') == str(value):
                        OrderProducts.objects.get(id=value).delete()
                        return redirect('order:edit-order', pk=self.object.pk)
        elif request.POST.get('add_product') == 'add product':
            product = request.POST.get('product')
            order = request.POST.get('order')
            quantity = request.POST.get('quantity')
            OrderProducts.objects.create(product_id=product, order_id=order, quantity=quantity)
            return redirect('order:edit-order', pk=self.object.pk)
        else:
            form = self.get_form()

            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)


class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_delete.html'
    success_url = reverse_lazy('order:order-list')
