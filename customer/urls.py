from django.urls import path
from customer.views import (CustomerListView, CustomerAddView, CustomerUpdateView, CustomerDeleteView,
                            CustomerAddressListView, CustomerAddressAddView, CustomerAddressUpdateView,
                            CustomerAddressDeleteView)

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer-list'),
    path('add', CustomerAddView.as_view(), name='add-customer'),
    path('update/<pk>', CustomerUpdateView.as_view(), name='update-customer'),
    path('delete/<pk>', CustomerDeleteView.as_view(), name='delete-customer'),
    path('address/', CustomerAddressListView.as_view(), name='customer-addresses'),
    path('address/add', CustomerAddressAddView.as_view(), name='add-addressr'),
    path('address/update/<pk>', CustomerAddressUpdateView.as_view(), name='update-address'),
    path('address/delete/<pk>', CustomerAddressDeleteView.as_view(), name='delete-address'),
]
