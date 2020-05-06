from django.contrib import admin

from inventory.models  import WareHouse,WareHouseManager,Category,Item,SaleProducts,BuyProducts,Sale,Buy
# Register your models here.

class WareHouseManagerInline(admin.TabularInline):
    model = WareHouseManager
    extra = 1     

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1  

class WareHouseAdmin(admin.ModelAdmin):
    model = WareHouse
    inlines = [WareHouseManagerInline]

class CategoryAdmin(admin.ModelAdmin):
    model = Category

class ItemAdmin(admin.ModelAdmin):
    model = Item

class SaleProductsInline(admin.TabularInline):
    model = SaleProducts
    extra = 1    
class SaleAdmin(admin.ModelAdmin):
    model = Sale
    inlines = [SaleProductsInline]

class BuyProductsInline(admin.TabularInline):
    model = BuyProducts
    extra = 1    
class BuyAdmin(admin.ModelAdmin):
    model = Buy 
    inlines = [BuyProductsInline]

class SaleProductsAdmin(admin.ModelAdmin):
    model = SaleProducts 

class BuyProductsAdmin(admin.ModelAdmin):
    model = BuyProducts 

admin.site.register(WareHouse, WareHouseAdmin) 
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Item, ItemAdmin) 
admin.site.register(Sale, SaleAdmin)  
admin.site.register(Buy, BuyAdmin)
#admin.site.register(SaleProducts, SaleProductsAdmin)
#admin.site.register(BuyProducts, BuyProductsAdmin)