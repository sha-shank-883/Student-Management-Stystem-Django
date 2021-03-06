from distutils.command.upload import upload
# import uuid
from email.policy import default
from pickle import NONE
from django.db import models

# from location_field.models.plain import PlainLocationField


standard = (
    ("1st", "1st"),
    ("2nd", "2nd"),
    ("3rd", "3rd"),
    ("4th", "4th"),
    ("5th", "5th"),
    ("6th", "6th"),
    ("7th", "7th"),
    ("8th", "8th"),
    ("9th", "9th"),
    ("10th", "10th"),
    ("11th", "11th"),
    ("12th", "12th"),
    ("Diploma", "Diploma"),
    ("Graduate", "Graduate"),
    ("Post Graduate", "Post Graduate"),
    ("PhD", "PhD"),
    ("Others", "Others"),
)


class Student(models.Model):
    Id = models.AutoField(primary_key=True)
    roll = models.IntegerField(default=1)
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=20)
    contact = models.CharField(max_length=20)
    standard = models.CharField(max_length=20, choices=standard, default="1st")
    img = models.ImageField(upload_to='images')
    # image = models.ImageField()

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=20)
    enquiry = models.CharField(max_length=50)
    phone = models.IntegerField()
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30, default='')
    email = models.EmailField(max_length=20)
    mobile = models.TextField(max_length=10, default=True)
    messsage = models.TextField(max_length=200)
    # maps = models.PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=20)
    message = models.TextField(max_length=300)

    def __str__(self):
        return self.fname


# class Student(models.Model):
#     id = models.IntegerField(primary_key=True)
#     rollno = models.IntegerField(max_length=30)
#     name = models.CharField(max_length=30)
#     city = models.CharField(max_length=50)
#     contact = models.EmailField(max_length=20)
#     std = models.TextField(max_length=300)
#     img = models.ImageField(upload_to="images")

#     def __str__(self):
#         return self.name

# class Search(models.Model):
#     stdname = models.CharField(max_length=20)
#     standard = models.CharField(max_length=20, choices=standard, default="1st")

#     def __str__(self):
#         return self.stdname
