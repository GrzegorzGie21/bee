from django.test import TestCase
from django.shortcuts import reverse
from django.urls import resolve

from employee.models import Employee, Document
from employee import views
from django.contrib.auth import get_user_model

from datetime import date


#Create your tests here.
class EmployeeTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='grzegorz',
                                                         password='haslo123')
        self.employee = Employee.objects.create(work_station='SAG',
                                                region='K-P',
                                                phone_number=501999000,
                                                user=self.user)

    def test_employee_string_representation(self):
        self.assertEqual(f'{self.employee.get_work_station_display()}', 'Sales agent')
        self.assertEqual(f'{self.employee.get_region_display()}', 'Kujawsko Pomorskie')
        self.assertEqual(f'{self.employee.phone_number}', '501999000')
        self.assertEqual(f'{self.employee.user}', 'grzegorz')

    def test_employee_list_view(self):
        response = self.client.get(reverse('employee:employee-list'))
        match = resolve('/employee/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Employee.objects.all().count(), 1)
        self.assertNotEqual(Employee.objects.all().count(), 4)
        self.assertContains(response, 'Employee list:')
        self.assertNotContains(response, 'Nothing to show')
        self.assertTemplateUsed(response, 'employee_list.html')
        self.assertEqual(match.func.__name__, views.EmployeeListView.as_view().__name__)

    def test_employee_detail_view(self):
        response = self.client.get(self.employee.get_absolute_url())
        no_response = self.client.get('/employee/99/')
        match = resolve(self.employee.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Work station:')
        self.assertTemplateUsed(response, 'employee_detail.html')
        self.assertEqual(match.func.__name__, views.EmployeeDetailView.as_view().__name__)

    def test_employee_edit_view(self):
        response = self.client.get(reverse('employee:edit-employee', args=[self.employee.pk]))
        no_response = self.client.get('employee/88/edit/')
        match = resolve('/employee/1/edit/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Edit employee:')
        self.assertTemplateUsed(response, 'employee_update.html')
        self.assertEqual(match.func.__name__, views.EmployeeEditView.as_view().__name__)

    def test_employee_delete_view(self):
        response = self.client.get(reverse('employee:delete-employee', args=[self.employee.pk]))
        no_response = self.client.get('/employee/88/delete/')
        match = resolve('/employee/1/delete/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Delete employee:')
        self.assertTemplateUsed(response, 'employee_delete.html')
        self.assertEqual(match.func.__name__, views.EmployeeDeleteView.as_view().__name__)

    def test_employee_create_view(self):
        response = self.client.get(reverse('employee:add-employee'))
        match = resolve('/employee/add/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Add employee:')
        self.assertTemplateUsed(response, 'employee_add.html')
        self.assertEqual(match.func.__name__, views.EmployeeCreateView.as_view().__name__)


class DocumentTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='grzegorz',
                                                         password='haslo123')
        self.document = Document.objects.create(title='Faktura',
                                                cost=12.99,
                                                created_date=date(2022,1,12).strftime('%Y-%m-%d'),
                                                type='C',
                                                user=self.user)

    def test_document_string_representation(self):
        self.assertEqual(f'{self.document.title}', 'Faktura')
        self.assertEqual(f'{self.document.cost}', '12.99')
        self.assertEqual(f'{self.document.created_date}', '2022-01-12')
        self.assertEqual(f'{self.document.get_type_display()}', 'Cash')
        self.assertEqual(f'{self.document.user}', 'grzegorz')

    def test_document_list_view(self):
        response = self.client.get(reverse('employee:document-list'))
        match = resolve('/employee/document/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Document.objects.all().count(), 1)
        self.assertNotEqual(Document.objects.all().count(), 4)
        self.assertContains(response, 'Document list:')
        self.assertNotContains(response, 'Nothing to show')
        self.assertTemplateUsed(response, 'document_list.html')
        self.assertEqual(match.func.__name__, views.DocumentListView.as_view().__name__)

    def test_document_detail_view(self):
        response = self.client.get(self.document.get_absolute_url())
        no_response = self.client.get('/employee/document/88/')
        match = resolve(self.document.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'Type:')
        self.assertTemplateUsed(response, 'document_detail.html')
        self.assertEqual(match.func.__name__, views.DocumentDetailView.as_view().__name__)