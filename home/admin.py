from django.contrib import admin
from .models import Report, Department

# Register your models here.

class ReportAdmin(admin.ModelAdmin):
    list_display = ('report_name', 'link_address', 'department')

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('department_name', 'date_created')

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Report, ReportAdmin)

