from django.urls import path
from customer.views import (CustomerListView, CustomerDetailView, CustomerAddView, CustomerUpdateView,
                            CustomerDeleteView, CustomerAddressListView, CustomerAddressDetailView,
                            CustomerAddressAddView, CustomerAddressUpdateView, CustomerAddressDeleteView)

app_name = 'customer'
urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),
    path('add/', CustomerAddView.as_view(), name='add-customer'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='edit-customer'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='delete-customer'),
    path('address/', CustomerAddressListView.as_view(), name='customer-addresses'),
    path('address/<int:pk>/', CustomerAddressDetailView.as_view(), name='address-detail'),
    path('address/add/', CustomerAddressAddView.as_view(), name='add-address'),
    path('address/<int:pk>/edit/', CustomerAddressUpdateView.as_view(), name='edit-address'),
    path('address/<int:pk>/delete/', CustomerAddressDeleteView.as_view(), name='delete-address'),
]
