from django.contrib import admin
from django.urls import path

from.views import *
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homePage,name="homePageUrl"),
    path('studentPage', studentPage,name="studentPageUrl"),
    path('teacherPage', teacherPage,name="teacherPageUrl"),
    path('employeePage',employeePage,name="employeePageUrl"),
    path('authorityPage',authorityPage,name="authorityPageUrl"),
    path('libraryPage',libraryPage,name="libraryPageUrl"),
    
    path('studentAdd',studentAdd,name="studentAdd"),
    path('teacherAdd',teacherAdd,name="teacherAdd"),
    path('employeeAdd',employeeAdd,name="employeeAdd"),
    path('authorityAdd',authorityAdd,name="authorityAdd"),
    path('libraryAdd',libraryAdd,name="libraryAdd"),
]
