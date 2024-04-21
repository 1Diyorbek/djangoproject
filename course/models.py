from django.db import models
from .helpes import PriceType


class Speciality(models.Model):
    title = models.CharField(max_length=20)
    image = models.ImageField(upload_to='speciality')
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Course(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField()
    active_user = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    slug = models.SlugField(null=False)
    price_type = models.CharField(max_length=10, choices=PriceType.choices, default=PriceType.dollar)
    image = models.ImageField(upload_to="course")
    rating = models.FloatField(default=5)
    speciality = models.ManyToManyField(Speciality)
    last_update = models.DateTimeField(auto_now=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
