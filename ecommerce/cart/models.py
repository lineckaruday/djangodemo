from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.



class Cart(models.Model):   #base class models.Model
   product=models.ForeignKey(Product,on_delete=models.CASCADE)       #product is a func used to connect a relation to another table ,so here product used to connect between Product and this Cart table
   user=models.ForeignKey(User,on_delete=models.CASCADE)          #user is a func used to connect a relation to another table ,so here user used to connect between User and this Cart table
   quantity=models.IntegerField()
   date_added=models.DateTimeField(auto_now_add=True)


   def subtotal(self):      #we can add func to class model  #here subtotal is a func to get total of that added quantity * product price
      return self.quantity*self.product.price     #this func calls from cart.html to work this func and that particular quantity and price multiplies here and shows in cart.html
                                                #current quantity and current price to multiplied here (self.qauntity*self.product.price)

   def __str__(self):
       return self.product.name        #to return each product name



   #so every user has a cart model,each time a user login and makes a product add to cart it stores in cart model




class Order(models.Model):
   product = models.ForeignKey(Product,on_delete=models.CASCADE)  # product is a func used to connect a relation to another table ,so here product used to connect between Product and this Cart table
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   no_of_items=models.IntegerField()
   ordered_date=models.DateTimeField(auto_now_add=True)
   address=models.TextField()
   phone=models.BigIntegerField()
   order_status=models.CharField(max_length=30,default="pending")     #just adding pending to show not delivered when product not delivered and shows delivered in default when product is delivered
   delivery_status=models.CharField(max_length=30,default="pending")

   def __str__(self):
      return self.user.username



class Account(models.Model):
   acctnum=models.BigIntegerField()
   accttype=models.CharField(max_length=20)
   amount=models.IntegerField()

   def __str__(self):
      return str(self.acctnum)

