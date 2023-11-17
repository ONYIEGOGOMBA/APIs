from django.db import models

# Create your models here.

class products(models.Model):
    product = models.CharField(max_length=50)
    price = models.DecimalField(decimal_place=2, max_digits=5)
    description = models.TextField(Default= 'Description')
    image = models.ImageField(upload_to="products", default="product.jpg")

def __str__(self):
        return self.product