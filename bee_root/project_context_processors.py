from django.utils import timezone
from django.conf import settings

def footer_cp(request):
    context = {'time': timezone.now(),
               'version': settings.APP_VERSION}
    return context