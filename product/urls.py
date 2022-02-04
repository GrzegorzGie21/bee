from django.urls import path
from .views import (ProductListView, ProductDetailView, ProductAddView, ProductUpdateView, ProductDeleteView,
                    PromotionListView, PromotionDetailView, PromotionAddView, PromotionEditView, PromotionDeleteView,
                    PackageListView, PackageDetailView, PackageAddView, PackageEditView, PackageDeleteView)

app_name = 'product'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('add/', ProductAddView.as_view(), name='add-product'),
    path('<int:pk>/edit/', ProductUpdateView.as_view(), name='edit-product'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='delete-product'),
    path('promotion/', PromotionListView.as_view(), name='promotion-list'),
    path('promotion/<int:pk>/', PromotionDetailView.as_view(), name='promotion-detail'),
    path('promotion/add/', PromotionAddView.as_view(), name='add-promotion'),
    path('promotion/<int:pk>/edit/', PromotionEditView.as_view(), name='edit-promotion'),
    path('promotion/<int:pk>/delete/', PromotionDeleteView.as_view(), name='delete-promotion'),
    path('package/', PackageListView.as_view(), name='package-list'),
    path('package/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
    path('package/add/', PackageAddView.as_view(), name='add-package'),
    path('package/<int:pk>/edit/', PackageEditView.as_view(), name='edit-package'),
    path('package/<int:pk>/delete/', PackageDeleteView.as_view(), name='delete-package'),
]
