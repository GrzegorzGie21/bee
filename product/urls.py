from django.urls import path
from .views import (ProductListView, ProductDetailView, ProductAddView, ProductUpdateView, ProductDeleteView,
                    PromotionListView, PromotionDetailView, PromotionAddView, PromotionEditView, PromotionDeleteView,
                    PackageListView, PackageDetailView, PackageAddView, PackageEditView, PackageDeleteView)

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('detail/<pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add/', ProductAddView.as_view(), name='add-product'),
    path('edit/<pk>/', ProductUpdateView.as_view(), name='edit-product'),
    path('delete/<pk>/', ProductDeleteView.as_view(), name='delete-product'),
    path('promotion/', PromotionListView.as_view(), name='promotion-list'),
    path('promotion/detail/<pk>/', PromotionDetailView.as_view(), name='promotion-detail'),
    path('promotion/add/', PromotionAddView.as_view(), name='add-promotion'),
    path('promotion/edit/<pk>/', PromotionEditView.as_view(), name='edit-promotion'),
    path('promotion/delete/<pk>/', PromotionDeleteView.as_view(), name='delete-promotion'),
    path('package/', PackageListView.as_view(), name='package-list'),
    path('package/detail/<pk>/', PackageDetailView.as_view(), name='package-detail'),
    path('package/add/', PackageAddView.as_view(), name='add-package'),
    path('package/edit/<pk>/', PackageEditView.as_view(), name='edit-package'),
    path('package/delete/<pk>/', PackageDeleteView.as_view(), name='delete-package'),
]
