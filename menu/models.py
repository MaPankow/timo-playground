from django.db import models

# Create your models here.

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name