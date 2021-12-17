from django.db import models

# Create your models here.
class OneModels(models.Model):
    nameMahath = models.CharField(max_length=20 , help_text='hello')
    number_mahatah = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nameMahath
    


class TheMahatah(models.Model):
    number_mahatah = models.ForeignKey("OneModels", verbose_name=("number_mahatah"), on_delete=models.CASCADE)
    owner = models.CharField(max_length=40, blank=True, null=True)
    manager_mahatah = models.CharField(max_length=40, blank=True, null=True)
    number_employees = models.ManyToManyField('Employee')
    number_pumps = models.IntegerField(blank=True, null=True)
    cars = models.ManyToManyField("Car")
    detaTime = models.DateField(auto_now=False)

    def __str__(self):
        return self.manager_mahatah
    


class Employee(models.Model):
    number_employee = models.IntegerField(blank=True, null=True)
    name_employee = models.CharField(max_length=50, blank=True, null=True)
    address_employee = models.CharField(max_length=50, blank=True, null=True)
    phone_employee = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name_employee


TYPE_CARS=[
        ('T','Toyota'),
        ('H','Honda'),
        ('M','Marcides'),
    ]
class Car(models.Model):
    
    owner_car = models.CharField(max_length=50)
    type_car = models.CharField(max_length=1 , choices=TYPE_CARS)
    number_car  = models.IntegerField()

    def __str__(self):
        return self.owner_car



class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name


    

    