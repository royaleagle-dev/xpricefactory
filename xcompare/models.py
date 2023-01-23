from django.db import models

# Create your models here.

class Product (models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

class Comparison (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    platform = models.CharField(max_length = 255)

    def __str__(self):
        return self.product.name

