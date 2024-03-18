from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("app:cook-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DishType(models.Model):
    name = models.CharField(max_length=63)

    def get_absolute_url(self):
        return reverse("app:dish-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cook = models.ManyToManyField(Cook, related_name="dishes")

    def __str__(self):
        return f"{self.name} {self.dish_type.name}"
