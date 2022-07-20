from django.db import models

# Create your models here.

class Reg(models.Model):
 name = models.CharField(max_length=30)
 email = models.EmailField(max_length=30)
 phone_no = models.CharField(max_length=30)
		
class Person(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    phone_no = models.CharField(max_length=30)
    blood_group = models.CharField(max_length=30)
    age = models.CharField(max_length=30)

class contact(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	contactnum = models.CharField(max_length=30)
	messege = models.CharField(max_length=150)
  
class Donor(models.Model):
	name = models.CharField(max_length=30)
	phone_no = models.CharField(max_length=30)
	date = models.CharField(max_length=30)
	time = models.CharField(max_length=30)

class Vol(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	messege = models.CharField(max_length=150)

class Supportus(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	phone = models.CharField(max_length=30)
	location = models.CharField(max_length=30)
	drive_date = models.CharField(max_length=30)
	messege = models.CharField(max_length=150)


    