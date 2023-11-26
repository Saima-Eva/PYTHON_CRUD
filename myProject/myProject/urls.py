from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from.views import *
  
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage', homePage,name="homePageUrl"),
    path('studentPage', studentPage,name="studentPageUrl"),
    path('teacherPage', teacherPage,name="teacherPageUrl"),
    path('employeePage',employeePage,name="employeePageUrl"),
    path('authorityPage',authorityPage,name="authorityPageUrl"),
    path('libraryPage',libraryPage,name="libraryPageUrl"),
    path('',loginPage,name="loginPage"),
    path('signupPage',signupPage,name="signupPage"),
    
    path('studentAdd',studentAdd,name="studentAdd"),
    path('teacherAdd',teacherAdd,name="teacherAdd"),
    path('employeeAdd',employeeAdd,name="employeeAdd"),
    path('authorityAdd',authorityAdd,name="authorityAdd"),
    path('libraryAdd',libraryAdd,name="libraryAdd"),
    
    
    path('editStudent/<str:myid>',editStudent, name="editStudent"),
    path('deleteStudent/<str:myid>',deleteStudent, name="deleteStudent"),
    path('updatestudent',updatestudent, name="updatestudent"),
    
    
    path('editTeacher/<str:myid>',editTeacher, name="editTeacher"),
    path('deleteTeacher/<str:myid>',deleteTeacher, name="deleteTeacher"),
    path('updateteacher',updateteacher, name="updateteacher"),
    
    path('editEmployee/<str:myid>',editEmployee, name="editEmployee"),
    path('deleteEmployee/<str:myid>',deleteEmployee, name="deleteEmployee"),
    path('updateemployee',updateemployee, name="updateemployee"),
    
    
    path('editAuthority/<str:myid>',editAuthority, name="editAuthority"),
    path('deleteAuthority/<str:myid>',deleteAuthority, name="deleteAuthority"),
    path('updateauthority',updateauthority, name="updateauthority"),
    
    path('editLibrary/<str:myid>',editLibrary, name="editLibrary"),
    path('deleteLibrary/<str:myid>',deleteLibrary, name="deleteLibrary"),
    path('updatelibrary',updatelibrary, name="updatelibrary"),
    
    
    path('myprofile',myprofile, name="myprofile"),
    
    

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

