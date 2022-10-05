from cmath import pi
from .models import *
from rest_framework import serializers
from rest_framework.validators import ValidationError
import re



class StudentCreateSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=20)
    name = serializers.CharField(max_length=20)
    surname = serializers.CharField(max_length=20)
    middlename = serializers.CharField(max_length=20)
    pinfl = serializers.CharField(max_length=14,validators=[])
    passport = serializers.CharField(max_length=9)
    phone = serializers.CharField(max_length=13)
    email = serializers.CharField(max_length=25)
    faculty = serializers.IntegerField()
    
     
    def validate_faculty(self,faculty):
        try:
            f = Faculty.objects.get(id=int(faculty))
            return f  
        except:
            raise ValidationError("faculty id raqami noto'g'ri !")
        

    def validate_pinfl(self,pinfl):

        if type(pinfl) == str and len(pinfl) == 14 and pinfl.isdigit():
            return pinfl
        else:
            raise ValidationError("Pinfl raqami noto'g'ri !")
       
    def create(self, clean_data):
        username = clean_data.pop("username")
        password = clean_data.pop("password")
        user = User.objects.create(username=username,password=password)
        clean_data['user'] = user
        student = Student.objects.create(**clean_data)
        return student
  

    
    
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    # def create(self, validated_data):





