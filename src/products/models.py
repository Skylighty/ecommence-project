from django.db import models

# Create your models here.
class Product(models.Model):
    name            = models.CharField(max_length=100)
    description     = models.TextField(blank=True)
    price           = models.DecimalField(max_digits=15, decimal_places=2) 
    onSale          = models.BooleanField(default=False)
    gallery         = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, default='https://redzonekickboxing.com/wp-content/uploads/2017/04/default-image-620x600.jpg')