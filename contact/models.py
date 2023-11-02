from django.db import models
from datetime import datetime    

ACTION_STATUS=(
    (0,'Action'),
    (1,'Pay'),
    (3,'View'),
    (4,'Edit'),
    (5,'Delete')
)

PAID_STATUS=(
    (0,'Checking'),
    (1,'Payment Done'),
    (2,'Due Running'),
    (3,'Return Due Running')
)

class Action(models.Model):
    Actions=models.IntegerField(choices=ACTION_STATUS,default=0)

    
class Suppliers(models.Model):
    Contact_ID=models.CharField(max_length=1000,unique=True)
    Business_Name=models.CharField(max_length=1000)
    Name=models.CharField(max_length=1000)
    Email=models.EmailField(max_length=1000,unique=True)
    Address=models.CharField(max_length=1000)
    Mobile=models.CharField(max_length=20,unique=True)
    Tax_Number=models.TextField(unique=True,blank=True)
    Pay_Term=models.CharField(max_length=1000)
    Total_Amount=models.TextField()
    Advance_Amount=models.TextField()
    Due_Amount=models.TextField()
    Return_Due_Amount=models.TextField()
    Paid_Status=models.IntegerField(choices=PAID_STATUS,default=0)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Contact_ID+' '+self.Email
    

class Customers(models.Model):
    Contact_ID=models.CharField(max_length=1000,unique=True)
    Business_Name=models.CharField(max_length=1000)
    Name=models.CharField(max_length=1000)
    Email=models.EmailField(max_length=1000,unique=True)
    Mobile=models.CharField(max_length=20,unique=True)
    Delivery_Address=models.CharField(max_length=1000)
    Home_Address=models.CharField(max_length=1000)
    Tax_Number=models.TextField(unique=True,blank=True)
    Credit_limit=models.TextField()
    Reward_Point=models.TextField()
    Customer_Group=models.CharField(max_length=1000)
    Pay_Term=models.CharField(max_length=1000)
    Opening_Balance=models.TextField()
    Advance_Balance=models.TextField()
    Total_Sale_Due=models.TextField()
    Total_Sell_Return_Due=models.TextField()
    Shipping_Address=models.CharField(max_length=1000)
    Created_At=models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.Contact_ID+self.Email
    
    