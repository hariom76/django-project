from django.db import models

# Create your models here.
class Registration(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=10, null=True)
    phone=models.CharField(max_length=15, null=True)
    dateofbirth = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.name

class OrderDetails(models.Model):
    order_price = models.CharField(max_length=3,null=True)
    order_name = models.CharField(max_length=3, null=True)
    order_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.order_name

class ItemsPrice(models.Model):
    Tea_Bread=50
    Paw_Bhagi=80
    Chhole_bhatoore=70
    Mutton_Curtlet=200
    Chicken_Biryani=150
    Paneer_Pakora=100
    Fish_Fry=125
    Burger=175
    Paneer=150
    Tadka=100
    Chowmin=75
    Egg_Roll=50
    Momo=125

