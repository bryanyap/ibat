from django.contrib import admin
from .models import Employee
from .models import Vendor
from .models import Project

# Register your models here.

admin.site.register(Employee)
admin.site.register(Vendor)
admin.site.register(Project)