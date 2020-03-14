from django.shortcuts import render

from django.urls import reverse_lazy
from .models import Product, Promotion, Package
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'


class ProductAddView(CreateView):
    model = Product
    template_name = 'product_add.html'
    fields = '__all__'
    success_url = reverse_lazy('product-list')


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('product-detail', args=[self.object.pk])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('customer-list')


class PromotionListView(ListView):
    model = Promotion
    template_name = 'promotion_list.html'


class PromotionDetailView(DetailView):
    model = Promotion
    template_name = 'promotion_detail.html'
    context_object_name = 'promotion'


class PromotionAddView(CreateView):
    model = Promotion
    template_name = 'promotion_add.html'
    fields = '__all__'
    success_url = reverse_lazy('promotion-list')


class PromotionEditView(UpdateView):
    model = Promotion
    template_name = 'promotion_update.html'
    fields = '__all__'
    context_object_name = 'promotion'

    def get_success_url(self):
        return reverse_lazy('promotion-detail', args=[self.object.pk])


class PromotionDeleteView(DeleteView):
    model = Promotion
    template_name = 'promotion_delete.html'
    success_url = reverse_lazy('promotion-list')


class PackageListView(ListView):
    model = Package
    template_name = 'package_list.html'


class PackageDetailView(DetailView):
    model = Package
    template_name = 'package_detail.html'


class PackageAddView(CreateView):
    model = Package
    template_name = 'package_add.html'
    fields = '__all__'
    success_url = reverse_lazy('package-list')


class PackageEditView(UpdateView):
    model = Package
    template_name = 'package_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('package-detail', args=[self.object.pk])


class PackageDeleteView(DeleteView):
    model = Package
    template_name = 'package_delete.html'
    success_url = reverse_lazy('package-list')