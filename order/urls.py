from django.urls import path
from .views import (OrderListView, OrderDetailView, OrderAddView, OrderUpdateView, OrderDeleteView)

app_name = 'order'
urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('add/', OrderAddView.as_view(), name='add-order'),
    path('<int:pk>/edit/', OrderUpdateView.as_view(), name='edit-order'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='delete-order'),
]
