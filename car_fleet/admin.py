from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Mileage)
class MileageAdmin(admin.ModelAdmin):
    pass

