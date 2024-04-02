from django.db import models

# Create your models here.

                  #for showing in home page to what category item to choose
class Category(models.Model):   #base class models.Model
    name = models.CharField(max_length=40)   #to add primary key : (max_length(20),primary key=true)
    desc = models.TextField()
    image=models.ImageField(upload_to='categories',null=True,blank=True)

    def __str__(self):
        return self.name



    #here product model definition for when choose 1 category details so that particular category item show many product so to add that product list

class Product(models.Model):
    name = models.CharField(max_length=40)  # to add primary key : (max_length(20),primary key=true)
    desc = models.TextField()
    image = models.ImageField(upload_to='products', null=True, blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)  #always set available stock default=true coz when we adding into table the stock is available we can change after that
    created=models.DateTimeField(auto_now_add=True)  #add one time into table
    updated=models.DateTimeField(auto_now=True)    #every time adds when we update record
    category=models.ForeignKey(Category,on_delete=models.CASCADE)  #the connection model must given inside (Category,on_delete=models.CASCADE) here Category is connection model
                  #category is a func used to connect a relation to another table ,so here category used to connect between Product and Category table
                     #inside on_delete is used to auto delete that particular product when the category table delets it (when in Category clothes is deleted so in Product table according to Clothes table Product records is auto deleted

                       #when adding records in Product admin we can see below a category drowndown related to Category table ,so it stores all data from Category table as object and connects with that particular drowpdown added with Product record

    def __str__(self):
        return self.name





