from django import forms
from django.contrib.auth import get_user_model

from .models import OrderProducts
from customer.models import Customer
from employee.models import Employee

class AddProductToOrderForm(forms.ModelForm):
    class Meta:
        model = OrderProducts
        fields = '__all__'
        widgets = {'order': forms.HiddenInput()}


def get_customers():
    return

class DailyReportForm(forms.Form):
    users = get_user_model().objects.all().values_list('id','last_name')
    date = forms.DateField(widget=forms.DateInput)
    user_id = forms.ChoiceField(choices=users)
