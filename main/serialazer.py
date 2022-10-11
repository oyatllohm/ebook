from rest_framework import serializers


from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializers(serializers.ModelSerializer):
    category = CategorySerializers(many = False)
    class Meta:
        
        model = Book
        # fields = '__all__'
        exclude = ('file',)
        
        
        
class DownlandSerializers(serializers.ModelSerializer):
    # category = CategorySerializers(many = False)
    class Meta:
        
        model = Book
        fields = ['id','file']
        # exclude = ('file',)
