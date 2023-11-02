from django.db import models
from .defaultValue import DURATION_TYPE,DURATION_TYPE,ALLOW_DECIMAL,BARCODE_TYPES,MANAGE_STOCK_CHOICES,EXPIRY_PERIOD_UNIT_CHOICES,TAX_TYPE_CHOICES,PRODUCT_TYPE_CHOICES,APPLICABLE_TAX_CHOICES

# Brand Model
class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    short_description = models.TextField()

    def __str__(self):
        return self.brand_name

# Category Model
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    category_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name


# Sub-Category Model
class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.subcategory_name
    

# Warranty Model
class Warranty(models.Model):
    warranty_name = models.CharField(max_length=100)
    warranty_description = models.TextField(blank=True)
    warranty_duration = models.PositiveIntegerField(default=1)
    warranty_duration_type = models.IntegerField(choices=DURATION_TYPE, default=0)

    def __str__(self):
        return self.warranty_name


# Unit Model
class Unit(models.Model):
    unit_name = models.CharField(max_length=100)
    unit_short_name = models.CharField(max_length=100,blank=True)
    allow_decimal = models.IntegerField(choices=ALLOW_DECIMAL)

    def __str__(self):
        return self.unit_name





#variations Type
class VariationType(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class VariationValue(models.Model):
    variation_type = models.ForeignKey(VariationType, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value

class ProductVariation(models.Model):
    variation_type = models.ForeignKey(VariationType, on_delete=models.CASCADE)
    variation_value = models.ForeignKey(VariationValue, on_delete=models.CASCADE)
    applicable_tax_name =models.IntegerField(choices=TAX_TYPE_CHOICES,default=0)
    selling_price_tax_type = models.IntegerField(choices=APPLICABLE_TAX_CHOICES,default=0)
    product_type =models.IntegerField(choices=PRODUCT_TYPE_CHOICES,default=0)


class ProductVariationValue(models.Model):
    product_variation =models.ForeignKey(ProductVariation, on_delete=models.CASCADE, blank=True, null=True) 
    exc_tax = models.DecimalField(max_digits=10, decimal_places=2)
    inc_tax = models.DecimalField(max_digits=10, decimal_places=2)
    margin_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    product_image = models.ImageField(upload_to='products/', null=True, blank=True)
    sku = models.CharField(max_length=50,blank=True)
    value = models.CharField(max_length=50,blank=True)

#Stock
class OpeningStock(models.Model):
    sku = models.CharField(max_length=255, unique=True)
    location = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField()
    unit_cost_before_tax = models.DecimalField(max_digits=10, decimal_places=2)
    lot_number = models.CharField(max_length=255, blank=True)
    expiry_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.sku

# Product Model
class AddProduct(models.Model):
    product_name = models.CharField(max_length=1000)
    sku = models.CharField(max_length=36, unique=True, editable=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)
    warranty = models.ForeignKey(Warranty, on_delete=models.CASCADE, blank=True)
    business_locations = models.CharField(max_length=1000)
    alert_quantity = models.PositiveIntegerField()
    barcode_type = models.IntegerField(choices=BARCODE_TYPES,default=0)
    manage_stock = models.IntegerField(choices=MANAGE_STOCK_CHOICES,default=0)
    expires_in = models.PositiveIntegerField(null=True,blank=True)
    expiry_period_unit = models.CharField(max_length=7,choices=EXPIRY_PERIOD_UNIT_CHOICES,null=True,blank=True)
    product_variation =models.ForeignKey(ProductVariationValue, on_delete=models.CASCADE, blank=True, null=True) 

    def __str__(self):
        return f"{self.product_name} (brand: {self.brand})"


