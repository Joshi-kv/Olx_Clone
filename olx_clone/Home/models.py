from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    
    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.CharField(max_length=250,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=150)
    model=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    owner_name=models.CharField(max_length=250)
    phone_no=models.CharField(max_length=10)
    image=models.ImageField( upload_to='Images', height_field=None, width_field=None, max_length=None)
    description=models.TextField(max_length=400,blank=True)