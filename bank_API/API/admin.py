from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Bank

# Register your models here.
@admin.register(Bank)
class BankAdmin(ImportExportModelAdmin):
    list_display = ('ifsc', 'bank_id', 'branch', 'address', 'city', 'district', 'state', 'bank_name')