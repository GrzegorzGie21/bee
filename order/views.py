from django.contrib.auth.mixins import PermissionRequiredMixin
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import edit

from .models import Order, OrderProducts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import AddProductToOrderForm, DailyReportForm


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


class OrderAddView(PermissionRequiredMixin, CreateView):
    permission_required = 'order_order_can_add_order'
    raise_exception = True
    permission_denied_message = 'Permission to this view is required'
    model = Order
    template_name = 'order_add.html'
    fields = ['date', 'user', 'customer']

    def form_valid(self, form):
        object = form.save()
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


class CreateDailyReportView(View):
    def get(self, request):
        form = DailyReportForm()
        context = {'form': form}
        return render(request, 'daily_report_form.html', context)

    def post(self, request):
        form = DailyReportForm(request.POST)
        if form.is_valid():
            date, user_id = form.cleaned_data.values()
            orders = Order.objects.filter(date=date, user=user_id)
            # print(orders)
            order_products = OrderProducts.objects.filter(order__in=orders)
            # for op in order_products:
            #     aggregate_quantity = op.aggregate(agg_quantity_sum=Sum('quantity'))
            #     annotate_quantity = op.annotate(ann_quantity_sum=Sum('quantity'))
            context = {'order_quantity': orders.count(),
                       'product_quantity': order_products.count(),
                       'result': True,
                       # 'aggregate_quantity_sum': aggregate_quantity,
                       # 'annotate_quantity_sum': annotate_quantity,
                       }
            return render(request, 'daily_report.html', context)
        else:
            context = {'form': form}
            return render(request, 'daily_report_form.html', context)


class DailyReportView(View):
    def get(self, request):
        return render(request, 'daily_report.html')

