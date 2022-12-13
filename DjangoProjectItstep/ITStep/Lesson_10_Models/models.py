from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name}, {self.price}"


class Department(models.Model):
    building = models.IntegerField(validators=[MaxLengthValidator(5), MinLengthValidator(1)], default=0)
    financing = models.DecimalField(max_digits=10, decimal_places=2, default=0, validators=[MinLengthValidator(0)])
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Disease(models.Model):
    name = models.CharField(max_length=100, unique=True)
    severity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13, validators=[RegexValidator("r^+380\d{9}$")], null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinLengthValidator(0.01)])
    surname = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Examination(models.Model):
    dayOfWeek = models.PositiveIntegerField([MinLengthValidator(1), MaxLengthValidator(7)], default=1)
    endTime = models.TimeField(null=False)
    name = models.CharField(max_length=100, unique=True)
    startTime = models.TimeField(null=False)

    def __str__(self):
        return f"{self.name}"


class Ward(models.Model):
    building = models.IntegerField(validators=[MinLengthValidator(1), MaxLengthValidator(5)])
    floor = models.IntegerField(validators=[MinLengthValidator(1)])
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.name}"


