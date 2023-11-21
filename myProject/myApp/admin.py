from django.contrib import admin

# Register your models here.

from myApp.models import Students
from myApp.models import Teachers
from myApp.models import Employees
from myApp.models import Authority
from myApp.models import Library

admin.site.register(Students)
admin.site.register(Teachers)
admin.site.register(Employees)
admin.site.register(Authority)
admin.site.register(Library)