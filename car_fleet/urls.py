from django.urls import path
from .views import (CarListView, CarCreateView, CarUpdateView, CarDeleteView, CarDetailView, MileageListView,
                    MileageCreateView, MileageUpdateView, MileageDeleteView, MileageDetailView)

app_name = 'car'
urlpatterns = [
    path('', CarListView.as_view(), name='car-list'),
    path('add/', CarCreateView.as_view(), name='add-car'),
    path('<pk>/', CarDetailView.as_view(), name='car-detail'),
    path('update/<pk>/', CarUpdateView.as_view(), name='update-car'),
    path('delete/<pk>/', CarDeleteView.as_view(), name='delete-car'),
    path('mileage/list/', MileageListView.as_view(), name='mileage-list'),
    path('mileage/add/', MileageCreateView.as_view(), name='add-mileage'),
    path('mileage/<pk>/', MileageDetailView.as_view(), name='mileage-detail'),
    path('mileage/update/<pk>/', MileageUpdateView.as_view(), name='update-mileage'),
    path('mileage/delete/<pk>/', MileageDeleteView.as_view(), name='delete-mileage'),

]
