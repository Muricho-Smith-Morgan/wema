from django.contrib import admin
from .models import Orphan

# Register your models here.
@admin.register(Orphan)
class RequestDemoAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'middle_name', 'last_name', 'gender', 'guardian', 'education_status', 'current_donor']