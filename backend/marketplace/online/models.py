from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator


# Create your models here.
class User(AbstractUser):
    phoneno=models.IntegerField(null=True)
    address=models.CharField(max_length=150)
    
class Product(models.Model):
    productpic=models.ImageField(upload_to='product_img',null=True)
    productname=models.CharField(max_length=100)
    category=models.CharField(max_length=100,null=True)
    color=models.CharField(max_length=120,null=True)
    price=models.IntegerField()
    quantity=models.IntegerField(null=True)
    description=models.CharField(max_length=300)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


class Reviews(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user') 
    review=models.CharField(max_length=100)
    rating=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    date=models.DateField(null=True,auto_now_add=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product',null=True)
    class Meta:
        unique_together=('user','product')
































