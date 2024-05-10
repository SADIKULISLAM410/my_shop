from django.contrib import admin
from product.models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parents','slug','status','create_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','title','slug','stock','is_available','create_date']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['category']
    #readonly_fields = ('image_tag')

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)