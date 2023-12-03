from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from myApp.models import *


@login_required
def homePage(request):

  student=Students.objects.filter(Marks__gt = 70)
  teacher=Teachers.objects.all()
  employee=Employees.objects.all()
  authority=Authority.objects.all()
  library=Library.objects.all()
  
  return render(request,"home.html", {'student':student, 'teacher':teacher, 'employee':employee, 'authority':authority, 'library':library})


@login_required
def myprofile(request):
   return render(request,"myprofile.html")

@login_required
def studentPage(request):
    student = Students.objects.all()

    context={
        "std":student,
    }

    return render(request,"student.html",context)



@login_required
def teacherPage(request):

    teacher = Teachers.objects.all()

    context={
        "tch":teacher,
    }

    return render(request,"teacher.html",context)


@login_required
def employeePage(request):

    employee = Employees.objects.all()

    context={
        "emp":employee,
    }

    return render(request,"employee.html",context)


def loginPage(request):
    myMessage={
        'Error_Message':'User Not Match',
        'Success_Message':'Login Successfully',
    }
    if request.method=='POST':
        user_name=request.POST.get("username")
        myPassword=request.POST.get("pass")
        
        
        user=authenticate(username=user_name, password=myPassword)
        if user:
            login(request, user)
            return redirect("homePageUrl")
        else:
            messages.warning(request, myMessage["Error_Message"])
        
    return render(request,"login.html")


def signupPage(request):
    
    myMessage={
        'Password_Error': 'Password and Confirm Password Not Match',
        'Password_Success': 'User Create Successfully',
    }
    if request.method=='POST':
        user_name=request.POST.get("username")
        myEmail=request.POST.get("email")
        pass1=request.POST.get("password1")
        pass2=request.POST.get("password2")
        
        if pass1 != pass2:
            messages.error(request, myMessage["Password_Error"])
        else:
            myusers = User.objects.create_user(user_name, myEmail, pass2)
            myusers.save()
            messages.success(request, myMessage['Password_Success'])
            return redirect("loginPage")

    return render(request,"signup.html")


def logoutPage(request):
    logout(request)
    return redirect("loginPage")
    


@login_required
def authorityPage(request):

    authority = Authority.objects.all()

    context={
        "auth":authority,
    }

    return render(request,"authority.html",context)

@login_required
def libraryPage(request):

    library = Library.objects.all()

    context={
        "lib":library,
    }

    return render(request,"library.html",context)


#Student Page
@login_required
def studentAdd(request):
    
    my_Messages={
        'Error_Message':'Student Add Failed',
        'Success_Message':'Student Add Successfully'
    }

    if request.method=="POST":

       fname=request.POST.get("fname")
       lname=request.POST.get("lname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       s_Marks=request.POST.get("Marks")
       profile_pic=request.FILES.get("profile_pic")
       
       print(profile_pic)
       
       student=Students(
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        Marks=s_Marks,

       )
       
       if profile_pic:
           student.profile_pic = profile_pic
       else:
           student.profile_pic = 'C:/Users/ROWTECH/Desktop/PYTHON_CRUD/myProject/media/media/profile_pic/default img.jpg'
          
       
       student.save()
       
       messages.success(request, my_Messages["Success_Message"])
    else:
        messages.error(request, my_Messages["Error_Message"])
           

    return redirect("studentPageUrl")

    return render(request, "student.html")

#Teacher Page
@login_required
def teacherAdd(request):
    
     my_Messages={
        'Error_Message':'Teacher Add Failed',
        'Success_Message':'Teacher Add Successfully'
    }

     if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        ID=request.POST.get("ID")
        myImage=request.FILES.get("profile_pic")
        
        print(myImage)

        teacher=Teachers(
            profile_pic=myImage,
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            ID=ID,

            )
        
        if myImage:
           teacher.profile_pic = myImage
        else:
           teacher.profile_pic = 'C:/Users/ROWTECH/Desktop/PYTHON_CRUD/myProject/media/media/profile_pic/default img.jpg'
        
        teacher.save()
        
        messages.success(request, my_Messages["Success_Message"])
        

        return redirect("teacherPageUrl")

     return render(request, "teacher.html")

#Employee Page
@login_required
def employeeAdd(request):
    
    my_Messages={
        'Error_Message':'Employee Add Failed',
        'Success_Message':'Employee Add Successfully'
    }

    if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        ID=request.POST.get("ID")
        myImage=request.FILES.get("profile_pic")
        
        print(myImage)

        employee=Employees(
            profile_pic=myImage,
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            ID=ID,

            )
        
        
        if myImage:
           employee.profile_pic = myImage
        else:
           employee.profile_pic = 'C:/Users/ROWTECH/Desktop/PYTHON_CRUD/myProject/media/media/profile_pic/default img.jpg'
        
        employee.save()
        
        messages.success(request, my_Messages["Success_Message"])

        return redirect("employeePageUrl")

    return render(request, "employee.html")


#Authority Page
@login_required
def authorityAdd(request):
    
     my_Messages={
        'Error_Message':'Authority Add Failed',
        'Success_Message':'Authority Add Successfully'
    }

     if request.method=="POST":

        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        mobile_num=request.POST.get("mobile")
        s_email=request.POST.get("email")
        s_age=request.POST.get("age")
        ID=request.POST.get("ID")
        myImage=request.FILES.get("profile_pic")
        
        print(myImage)

        authority=Authority(
            profile_pic=myImage,
            First_Name=fname,
            Last_Name=lname,
            Mobile=mobile_num,
            Email=s_email,
            Age=s_age,
            ID=ID,

            )
        
        if myImage:
           authority.profile_pic = myImage
        else:
           authority.profile_pic = 'C:/Users/ROWTECH/Desktop/PYTHON_CRUD/myProject/media/media/profile_pic/default img.jpg'
        
        authority.save()
        
        messages.success(request, my_Messages["Success_Message"])


        return redirect("authorityPageUrl")

     return render(request, "authority.html")

#Library Page
@login_required
def libraryAdd(request):
    
    my_Messages={
        'Error_Message':'Book Add Failed',
        'Success_Message':'Book Add Successfully'
    }

    if request.method=="POST":

        book=request.POST.get("b_name")
        writer=request.POST.get("w_name")
        s_num=request.POST.get("Serial_No")
        a_date=request.POST.get("Acquisition_Date")
        r_date=request.POST.get("Return_Date")
        ID=request.POST.get("ID")
        myImage=request.FILES.get("profile_pic")
        
        print(myImage)

        library=Library(
            profile_pic=myImage,
            Book_Name=book,
            Writer_Name=writer,
            Serial_No=s_num,
            Acquisition_Date=a_date,
            Return_Date=r_date,
            ID=ID,

            )
        library.save()
        
        messages.success(request, my_Messages["Success_Message"])
        
        if myImage:
           library.profile_pic = myImage
        else:
           library.profile_pic = 'C:/Users/ROWTECH/Desktop/PYTHON_CRUD/myProject/media/media/profile_pic/default img.jpg'

        return redirect("libraryPageUrl")

    return render(request, "library.html")



#Student Update
@login_required
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
       s_Marks=request.POST.get("Marks")
       profile_pic=request.FILES.get("profile_pic")

       student=Students(
        id=studentid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        Marks=s_Marks,
        profile_pic=profile_pic,

       )
       student.save()

       return redirect("studentPageUrl")
    
    
#Teacher Update
@login_required
def editTeacher(request, myid):
    teacher=Teachers.objects.filter(id=myid)
    context={
        "teacher":teacher,
    }
    return render(request, "editTeacher.html", context)  

@login_required
def deleteTeacher(request, myid):
    teacher=Teachers.objects.filter(id=myid)
    teacher.delete()
    return redirect("teacherPageUrl")


@login_required
def updateteacher(request):

    if request.method=="POST":
    
       teacherid=request.POST.get("teacherid")
       fname=request.POST.get("firstname")
       lname=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       ID=request.POST.get("ID")
       profile_pic=request.FILES.get("profile_pic")

       teacher=Teachers(
        id=teacherid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        ID=ID,
        profile_pic=profile_pic,

       )
       teacher.save()

       return redirect("teacherPageUrl")
   
   
#Employee update
@login_required
def editEmployee(request, myid):
    employee=Employees.objects.filter(id=myid)
    context={
        "employee":employee,
    }
    return render(request, "editEmployee.html", context)  

@login_required
def deleteEmployee(request, myid):
    employee=Employees.objects.filter(id=myid)
    employee.delete()
    return redirect("employeePageUrl")


@login_required
def updateemployee(request):

    if request.method=="POST":
    
       employeeid=request.POST.get("employeeid")
       fname=request.POST.get("firstname")
       lname=request.POST.get("lastname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       ID=request.POST.get("ID")
       profile_pic=request.FILES.get("profile_pic")

       employee=Employees(
        id=employeeid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        ID=ID,
        profile_pic=profile_pic,

       )
       employee.save()

       return redirect("employeePageUrl")
   
   
#Authority update
@login_required
def editAuthority(request, myid):
    authority=Authority.objects.filter(id=myid)
    context={
        "authority":authority,
    }
    return render(request, "editAuthority.html", context)  

@login_required
def deleteAuthority(request, myid):
    authority=Authority.objects.filter(id=myid)
    authority.delete()
    return redirect("authorityPageUrl")


@login_required
def updateauthority(request):

    if request.method=="POST":
    
       authorityid=request.POST.get("authorityid")
       fname=request.POST.get("fname")
       lname=request.POST.get("lname")
       mobile_num=request.POST.get("mobile")
       s_email=request.POST.get("email")
       s_age=request.POST.get("age")
       ID=request.POST.get("ID")
       profile_pic=request.FILES.get("profile_pic")

       authority=Authority(
        id=authorityid, 
        First_Name=fname,
        Last_Name=lname,
        Mobile=mobile_num,
        Email=s_email,
        Age=s_age,
        ID=ID,
        profile_pic=profile_pic,

       )
       authority.save()

       return redirect("authorityPageUrl")
   
   
#Library update
@login_required
def editLibrary(request, myid):
    library=Library.objects.filter(id=myid)
    context={
        "library":library,
    }
    return render(request, "editLibrary.html", context)  

@login_required
def deleteLibrary(request, myid):
    library=Library.objects.filter(id=myid)
    library.delete()
    return redirect("libraryPageUrl")

@login_required
def updatelibrary(request):

    if request.method=="POST":
    
       Libraryid=request.POST.get("libraryid")
       b_name=request.POST.get("b_name")
       w_name=request.POST.get("w_name")
       Serial_No=request.POST.get("Serial_No")
       Acquisition_Date=request.POST.get("Acquisition_Date")
       r_date=request.POST.get("r_date")
       ID=request.POST.get("ID")
       profile_pic=request.FILES.get("profile_pic")

    library=Library(
        id=Libraryid, 
        Book_Name=b_name,
        Writer_Name=w_name,
        Serial_No=Serial_No,
        Acquisition_Date=Acquisition_Date,
        Return_Date=r_date,
        ID=ID,
        profile_pic=profile_pic,

       )
    library.save()

    return redirect("libraryPageUrl")
   

   
