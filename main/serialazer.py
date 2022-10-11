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

class ContactSerializers(serializers.Serializer):
    # student = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=100 , allow_blank = True)
    email = serializers.EmailField(max_length=100 , allow_blank = True)
    subject = serializers.CharField(max_length=100 , allow_blank = True)
    msg = serializers.CharField(max_length=500)

    def save(self, validated_data,student= None):
        if student:
            validated_data['student'] =student
            contact =  Contact.objects.create(**validated_data)
            return contact
            
            
        if validated_data.get('name') and validated_data.get('email'):
            return  Contact.objects.create(**validated_data)
        else:
            return None
