from django.urls import path
from .views import (EmployeeListView, EmployeeCreateView, EmployeeDetailView, EmployeeEditView, EmployeeDeleteView,
                    DocumentListView, DocumentCreateView, DocumentDetailView, DocumentEditView, DocumentDeleteView)

urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('add/', EmployeeCreateView.as_view(), name='add-employee'),
    path('detail/<pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('edit/<pk>/', EmployeeEditView.as_view(), name='edit-employee'),
    path('delete/<pk>/', EmployeeDeleteView.as_view(), name='delete-employee'),
    path('documents/', DocumentListView.as_view(), name='document-list'),
    path('document/add/', DocumentCreateView.as_view(), name='add-document'),
    path('document/<pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('document/edit/<pk>/', DocumentEditView.as_view(), name='edit-document'),
    path('document/delete/<pk>/', DocumentDeleteView.as_view(), name='delete-document'),
]
