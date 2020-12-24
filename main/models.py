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