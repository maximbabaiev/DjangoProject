import datetime

from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator


# Create your models here.

class Curator(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.surname}"


class Facultie(models.Model):
    financing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinLengthValidator(0)], default=0)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}, {self.financing}"


class Department(models.Model):
    building = models.IntegerField(choices=(
        (
            1, 1
        ), (
            2, 2
        ), (
            3, 3
        ), (
            4, 4
        ), (
            5, 5
        )
    ), blank=True)
    financing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinLengthValidator(0)], default=0)
    name = models.CharField(max_length=100, unique=True)
    facultyId = models.ForeignKey(Facultie, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.financing}"


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)
    year = models.IntegerField(choices=(
        (
            1, 1
        ), (
            2, 2
        ), (
            3, 3
        ), (
            4, 4
        ), (
            5, 5
        )
    ), blank=True)
    departmentId = models.ForeignKey(Department, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.name}, {self.year}"


class GroupsCurator(models.Model):
    curatorId = models.ForeignKey(Curator, on_delete=models.CASCADE)
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.curatorId}, {self.groupId}"


class Teacher(models.Model):
    isProfessor = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinLengthValidator(0.01)])
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.salary}"


class Subject(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name}"


class Lecture(models.Model):
    date = models.DateTimeField(auto_now=False)
    lectureRoom = models.CharField(max_length=100)
    subjectId = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.lectureRoom}, {self.subjectId}, {self.teacherId}, {self.date}"


class GroupsLecture(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    lectureId = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.groupId}, {self.lectureId}"


class Students(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=(
        (
            0, 0
        ), (
            1, 1
        ), (
            2, 2
        ), (
            3, 3
        ), (
            4, 4
        ), (
            5, 5
        )
    ))
    surname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.rating}"


class GroupsStudent(models.Model):
    groupId = models.ForeignKey(Group, on_delete=models.CASCADE)
    studentId = models.ForeignKey(Students, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.groupId}, {self.studentId}"