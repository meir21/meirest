from django.db import models


# Create your models here.


class Branch(models.Model):
    name = models.CharField(max_length=32, null=False)
    address = models.CharField(max_length=1024, null=False)
    image_url = models.CharField(max_length=512)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=64, null=False)
    price = models.FloatField(null=True, blank=True, default=None)

    class Meta:
        verbose_name_plural = "Toppings"

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=32, null=False)
    description = models.TextField(max_length=2048, null=True, blank=True)
    price = models.FloatField(null=True, blank=True,default=None)
    image_url = models.CharField(max_length=512)
    toppings = models.ManyToManyField(Topping, related_name='belonged_dishes', blank=True)

    class Meta:
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name

