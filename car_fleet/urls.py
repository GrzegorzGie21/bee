from django.urls import path
from .views import CarListView, CarCreateView, CarUpdateView, CarDeleteView, CarDetailView

urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('add', CarCreateView.as_view(), name='add-car'),
    path('<pk>', CarDetailView.as_view(), name='car-detail'),
    path('update/<pk>', CarUpdateView.as_view(), name='update-car'),
    path('delete/<pk>', CarDeleteView.as_view(), name='delete-car'),
]