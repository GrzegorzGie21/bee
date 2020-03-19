from django import forms
from .models import OrderProducts

class AddProductToOrderForm(forms.ModelForm):
    class Meta:
        model = OrderProducts
        fields = '__all__'
        widgets = {'order': forms.HiddenInput()}