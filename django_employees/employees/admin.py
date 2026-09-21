from django.contrib import admin
from .models import Department,Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['id','full_name','email','salary']
    list_filter=['manager']
    search_fields=['full_name','email']
    list_editable=['salary']
    ordering=['id']

# Register your models here.
admin.site.register(Department)
admin.site.register(Employee,EmployeeAdmin)