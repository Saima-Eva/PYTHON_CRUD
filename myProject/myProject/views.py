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

       fname=request.POST.get("firstname")
       lname=request.POST.get("lastname")
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

        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
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

        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
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

        fname=request.POST.get("firstname")
        lname=request.POST.get("lastname")
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

        bname=request.POST.get("Book_Name")
        wname=request.POST.get("Writer_Name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")

        library=Library(
            Book_Name=bname,
            Writer_Name=wname,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,

            )
        library.save()

        return redirect("libraryPageUrl")

    return render(request, "library.html")
