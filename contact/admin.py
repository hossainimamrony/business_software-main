from django.contrib import admin
from .models import Suppliers,Customers

class Suppliers_Column_Display(admin.ModelAdmin):
    list_display=('Contact_ID','Business_Name','Name','Email','Address','Mobile','Tax_Number','Pay_Term','Total_Amount','Advance_Amount','Due_Amount','Return_Due_Amount','Paid_Status')
admin.site.register(Suppliers,Suppliers_Column_Display)



class Customers_Column_Display(admin.ModelAdmin):
    list_display=('Contact_ID','Business_Name','Name','Email','Mobile','Delivery_Address','Home_Address','Tax_Number','Credit_limit','Reward_Point','Customer_Group','Pay_Term','Opening_Balance','Advance_Balance','Total_Sale_Due','Total_Sell_Return_Due','Shipping_Address')
admin.site.register(Customers,Customers_Column_Display)