from django.contrib import admin
from .models import *
# Register your models here.

from django.utils.safestring import mark_safe
admin.site.register(Faculty)
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display =  ['id','title','desc',
               'get_image']
    search_fields = ['title']
    def get_image(self,obj):
        
        return mark_safe(f"<img src = '{obj.image.url}' width = '150px' >")

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display =  ['id','title','desc',
               'get_image']
    search_fields = ['title']
    def get_image(self,obj):
        return mark_safe(f"<img src = '{obj.image.url}' width = '150px' >")