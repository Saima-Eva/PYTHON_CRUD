from django.shortcuts import redirect, render
from myApp.models import *


def homePage(request):
   return render(request,"home.html")


def studentPage(request):
    student = Students.objects.all()

    context={
        "std":student,
    }

    return render(request,"student.html",context)


def teacherPage(request):

    teacher = Teachers.objects.all()

    context={
        "tch":teacher,
    }

    return render(request,"teacher.html",context)


def employeePage(request):

    employee = Employees.objects.all()

    context={
        "emp":employee,
    }

    return render(request,"employee.html",context)

def loginPage(request):

    return render(request,"login.html")

def signupPage(request):

    return render(request,"signup.html")


def authorityPage(request):

    authority = Authority.objects.all()

    context={
        "auth":authority,
    }

    return render(request,"authority.html",context)


def libraryPage(request):

    library = Library.objects.all()

    context={
        "lib":library,
    }

    return render(request,"library.html",context)


#Student Page
def studentAdd(request):

    if request.method=="POST":

       fname=request.POST.get("fname")
       lname=request.POST.get("lname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")

       student=Students(
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,

       )
       student.save()

       return redirect("studentPageUrl")

    return render(request, "student.html")

#Teacher Page
def teacherAdd(request):

    if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")

        teacher=Teachers(
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,

            )
        teacher.save()

        return redirect("teacherPageUrl")

    return render(request, "teacher.html")

#Employee Page
def employeeAdd(request):

    if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")

        employee=Employees(
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,

            )
        employee.save()

        return redirect("employeePageUrl")

    return render(request, "employee.html")


#Authority Page
def authorityAdd(request):

    if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")

        authority=Authority(
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,

            )
        authority.save()

        return redirect("authorityPageUrl")

    return render(request, "authority.html")

#Library Page
def libraryAdd(request):

    if request.method=="POST":

        book=request.POST.get("b_name")
        writer=request.POST.get("w_name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")

        library=Library(
            Book_Name=book,
            Writer_Name=writer,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,

            )
        library.save()

        return redirect("libraryPageUrl")

    return render(request, "library.html")



#Student Update
def editStudent(request, myid):
    student=Students.objects.filter(id=myid)
    context={
        "student":student,
    }
    return render(request, "editStudent.html", context)



def deleteStudent(request, myid):
    student=Students.objects.filter(id=myid)
    student.delete()
    return redirect("studentPageUrl")


def updatestudent(request):

    if request.method=="POST":
    
       studentid=request.POST.get("studentid")
       fname=request.POST.get("fname")
       lname=request.POST.get("lname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")

       student=Students(
        id=studentid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,

       )
       student.save()

       return redirect("studentPageUrl")
    
    
#Teacher Update
def editTeacher(request, myid):
    teacher=Teachers.objects.filter(id=myid)
    context={
        "teacher":teacher,
    }
    return render(request, "editTeacher.html", context)  

def deleteTeacher(request, myid):
    teacher=Teachers.objects.filter(id=myid)
    teacher.delete()
    return redirect("teacherPageUrl")


def updateteacher(request):

    if request.method=="POST":
    
       teacherid=request.POST.get("teacherid")
       fname=request.POST.get("firstname")
       lname=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")

       teacher=Teachers(
        id=teacherid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,

       )
       teacher.save()

       return redirect("teacherPageUrl")
   
   
#Employee update
def editEmployee(request, myid):
    employee=Employees.objects.filter(id=myid)
    context={
        "employee":employee,
    }
    return render(request, "editEmployee.html", context)  

def deleteEmployee(request, myid):
    employee=Employees.objects.filter(id=myid)
    employee.delete()
    return redirect("employeePageUrl")


def updateemployee(request):

    if request.method=="POST":
    
       employeeid=request.POST.get("employeeid")
       fname=request.POST.get("firstname")
       lname=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")

       employee=Employees(
        id=employeeid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,

       )
       employee.save()

       return redirect("employeePageUrl")
   
   
#Authority update
def editAuthority(request, myid):
    authority=Authority.objects.filter(id=myid)
    context={
        "authority":authority,
    }
    return render(request, "editAuthority.html", context)  

def deleteAuthority(request, myid):
    authority=Authority.objects.filter(id=myid)
    authority.delete()
    return redirect("authorityPageUrl")


def updateauthority(request):

    if request.method=="POST":
    
       authorityid=request.POST.get("authorityid")
       fname=request.POST.get("fname")
       lname=request.POST.get("lname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")

       authority=Authority(
        id=authorityid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,

       )
       authority.save()

       return redirect("authorityPageUrl")
   
   
#Library update
def editLibrary(request, myid):
    library=Library.objects.filter(id=myid)
    context={
        "library":library,
    }
    return render(request, "editLibrary.html", context)  

def deleteLibrary(request, myid):
    library=Library.objects.filter(id=myid)
    library.delete()
    return redirect("libraryPageUrl")


def updatelibrary(request):

    if request.method=="POST":
    
       Libraryid=request.POST.get("libraryid")
       b_name=request.POST.get("b_name")
       w_name=request.POST.get("w_name")
       Serial_No=request.POST.get("Serial_No")
       Acquisition_Date=request.POST.get("Acquisition_Date")
       r_date=request.POST.get("r_date")

    library=Library(
        id=Libraryid, 
        Book_Name=b_name,
        Writer_Name=w_name,
        Serial_No=Serial_No,
        Acquisition_Date=Acquisition_Date,
        Return_Date=r_date,

       )
    library.save()

    return redirect("libraryPageUrl")
   

    
