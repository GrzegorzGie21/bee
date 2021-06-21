from django.utils import timezone

def footer_cp(request):
    context = {'time': timezone.now(),
               'version': '1.0'}
    return context