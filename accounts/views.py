from django.contrib.auth import get_user_model
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreateUserForm

User = get_user_model()


# Create your views here.
class RegistrationView(CreateView):
    form_class = CreateUserForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
