from django.db import models

# Create your models here.

class Students(models.Model):
    First_Name=models.CharField(max_length=100,null=True)
    Last_Name=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=100,null=True)
    Email=models.CharField(max_length=100,null=True)
    Age=models.CharField(max_length=100,null=True)
    Marks=models.IntegerField(max_length=100, null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)

    def __str__(self):
     return self.First_Name+" "+self.Last_Name


class Teachers(models.Model):
    First_Name=models.CharField(max_length=100)
    Last_Name=models.CharField(max_length=100)
    Mobile=models.CharField(max_length=100)
    Email=models.CharField(max_length=100)
    Age=models.CharField(max_length=100)
    ID=models.IntegerField(max_length=100, null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)

    def __str__(self):
        return self.First_Name+" "+self.Last_Name



class Employees(models.Model):
    First_Name=models.CharField(max_length=100, null=True)
    Last_Name=models.CharField(max_length=100, null=True)
    Mobile=models.CharField(max_length=100, null=True)
    Email=models.CharField(max_length=100, null=True)
    Age=models.CharField(max_length=100, null=True)
    ID=models.IntegerField(max_length=100, null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)

    def __str__(self):
     return self.First_Name+" "+self.Last_Name
    

class Authority(models.Model):
    First_Name=models.CharField(max_length=100, null=True)
    Last_Name=models.CharField(max_length=100, null=True)
    Mobile=models.CharField(max_length=100, null=True)
    Email=models.CharField(max_length=100, null=True)
    Age=models.CharField(max_length=100, null=True)
    ID=models.IntegerField(max_length=100, null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)

    def __str__(self):
     return self.First_Name+" "+self.Last_Name
    

class Library(models.Model):
    Book_Name=models.CharField(max_length=100, null=True)
    Writer_Name=models.CharField(max_length=100, null=True)
    Serial_No=models.CharField(max_length=100, null=True)
    Acquisition_Date=models.CharField(max_length=100, null=True)
    Return_Date=models.CharField(max_length=100, null=True)
    ID=models.IntegerField(max_length=100, null=True)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)

    def __str__(self):
     return self.Book_Name+" "+self.Writer_Name