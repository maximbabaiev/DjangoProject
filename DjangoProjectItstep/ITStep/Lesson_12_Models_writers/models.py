import base64
from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator, RegexValidator


# Create your models here.

class Book(models.Model):
    nameBook = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    yearCreate = models.DateField()
    public = models.CharField(max_length=100)
    available = models.BooleanField(default=True)
    img = models.ImageField(upload_to="images/")
    img_base64 = models.CharField(max_length=200000, blank=True)
    style = models.CharField(max_length=100, choices=(
        (
            "Фэнтези", "Фэнтези"
        ), (
            "Детективы", "Детективы"
        )
    ))

    def save(self, *args, **kwargs):
        self.img_base64 = base64.b64encode(self.img.read()).decode("utf-8")
        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.nameBook}, {self.author}, {self.yearCreate}, {self.style}"