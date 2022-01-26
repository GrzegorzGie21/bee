from django.urls import path
from .views import (EmployeeListView, EmployeeCreateView, EmployeeDetailView, EmployeeEditView, EmployeeDeleteView,
                    DocumentListView, DocumentCreateView, DocumentDetailView, DocumentEditView, DocumentDeleteView,
                    RegisterUserView, LoginView, LogoutView)

app_name = 'employee'
urlpatterns = [
    path('', EmployeeListView.as_view(), name='employee-list'),
    path('add/', EmployeeCreateView.as_view(), name='add-employee'),
    path('<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
    path('<int:pk>/edit/', EmployeeEditView.as_view(), name='edit-employee'),
    path('<int:pk>/delete/', EmployeeDeleteView.as_view(), name='delete-employee'),
    path('document/', DocumentListView.as_view(), name='document-list'),
    path('document/add/', DocumentCreateView.as_view(), name='add-document'),
    path('document/<int:pk>/', DocumentDetailView.as_view(), name='document-detail'),
    path('document/<int:pk>/edit/', DocumentEditView.as_view(), name='edit-document'),
    path('document/<int:pk>/delete/', DocumentDeleteView.as_view(), name='delete-document'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
