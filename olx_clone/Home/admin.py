from django.contrib import admin
from . models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['name','slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,CategoryAdmin)    

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','model','price','location','owner_name','phone_no']
    prepopulated_fields={'slug':('name',)}
    list_per_page=20
    
admin.site.register(Product,ProductAdmin)