from django.db import models
from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,ShippingAddress,BillingAddress

class WareHouse(BaseModel):
	code        =  models.CharField(max_length=255, blank=True, null=True) 
	name        =  models.CharField(max_length=255, blank=True, null=True) 
	location    =  models.CharField(max_length=255, blank=True, null=True) 
	date_start  = models.DateField( blank=True, null=True)
	date_end  = models.DateField( blank=True, null=True)
	status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 
	def __str__(self):
	    return self.name

class WareHouseManager(models.Model):
	warehouse       = models.ForeignKey(WareHouse, blank=True, null=True,on_delete=models.CASCADE)
	manager         = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
	appointed_date  = models.DateField( blank=True, null=True)
	date_end        = models.DateField( blank=True, null=True)
	status          = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 

class Category(models.Model):
	parent_category  = models.ForeignKey('self', blank=True, null=True, default=None, related_name='category_item',on_delete=models.CASCADE)
	name             = models.CharField(max_length=255, blank=True, null=True) 
	description      = models.TextField(blank=True, null=True)
	slug             = models.CharField(max_length=255, blank=True, null=True) 
	def __str__(self):
	    return self.name

class Item(models.Model):
	warehouse     = models.ForeignKey(WareHouse, blank=True, null=True,on_delete=models.CASCADE)
	category      = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE)
	name          = models.CharField(max_length=255, blank=True, null=True) 
	brand         = models.CharField(max_length=255, blank=True, null=True) 
	model         = models.CharField(max_length=255, blank=True, null=True) 
	item_unit     = models.ForeignKey(Unit, blank=True, null=True,on_delete=models.CASCADE)
	item_quantity = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	orginal_price = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	sale_price    = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	date_added    = models.DateField( blank=True, null=True)
	slug          = models.CharField(max_length=255, blank=True, null=True) 


class Sale(BaseModel):
    customer         = models.ForeignKey(Customer, blank=True, null=True,on_delete=models.CASCADE)
    seller           = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)	
    shipping_address = models.ForeignKey(ShippingAddress, blank=True, null=True,on_delete=models.CASCADE)
    billing_address  = models.ForeignKey(BillingAddress, blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('order_submitted','order_submitted'),('shipping','shipping'),('completed','completed'),('back','back'),('order_cancel','order_cancel')), blank=True) 

class SaleProducts(models.Model):
	sale         = models.ForeignKey(Sale, blank=True, null=True,on_delete=models.CASCADE)
	item         = models.ForeignKey(Item, blank=True, null=True,on_delete=models.CASCADE)
	unit         = models.ForeignKey(Unit, blank=True, null=True,on_delete=models.CASCADE)
	quantity     = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	discount     = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	tax          = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	date_added   = models.DateField( blank=True, null=True)
	slug         = models.CharField(max_length=255, blank=True, null=True) 



class Buy(models.Model):
    customer         = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
    seller           = models.ForeignKey(Customer, blank=True, null=True,on_delete=models.CASCADE)
    shipping_address = models.ForeignKey(ShippingAddress, blank=True, null=True,on_delete=models.CASCADE)
    billing_address  = models.ForeignKey(BillingAddress, blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('order_submitted','order_submitted'),('shipping','shipping'),('completed','completed'),('back','back'),('order_cancel','order_cancel')), blank=True) 


class BuyProducts(models.Model):
	buy          = models.ForeignKey(Buy, blank=True, null=True,on_delete=models.CASCADE)
	item         = models.ForeignKey(Item, blank=True, null=True,on_delete=models.CASCADE)
	unit         = models.ForeignKey(Unit, blank=True, null=True,on_delete=models.CASCADE)
	quantity     = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	discount     = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	tax          = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
	date_added   = models.DateField( blank=True, null=True)
	slug         = models.CharField(max_length=255, blank=True, null=True) 

