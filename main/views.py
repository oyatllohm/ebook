from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from reader.error_status import *
from reader.serializer import  StudentSerializer
from reader.models import Student
from rest_framework.response import Response
# Create your views here.
from .models import *
from rest_framework.authentication import TokenAuthentication
from .serialazer import CategorySerializers , BookSerializers , DownlandSerializers , ContactSerializers
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import AllowAny,IsAdminUser,IsAuthenticated

from django.http import FileResponse
import base64
# Stepik.org
class Get_student(APIView):
    
    # authentication_classes = TokenAuthentication
    def post(self,request):
        passport = request.data.get('passport')

        if passport is None:
            return Response({
                'Error_status':PASSPORT_NUMBER_NOD_SEND,
                'status':'Error'
            })

        try:
            user = User.objects.get(username=passport)
            student = Student.objects.get(user=user)
        except:
            return Response({'Error_status':USER_NOT_FOUND,
                'status':'Error'})
        serializer = StudentSerializer(student,many = False)
        return Response({'Error_status':SUCCESS,
                        'status':'ok',
                     'data': serializer.data})


class CategoryApiView(ViewSet):
    def list(self, request):
        # print(request.method) # GET,POST,PUT,UPDATE,DELETE
        queryset = Category.objects.all()
        serializer = CategorySerializers(queryset, many=True)
        return Response({

            "categories":serializer.data
        })
    def retrive(self,request,pk):
        # print(request.method) # GET,POST,PUT,UPDATE,DELETE
        try:

            queryset = Category.objects.get(id= int(pk))
        except:
            return Response({

            "categories":NOT_FOUND
        })
        boks = Book.objects.filter(category=queryset)
        serilizer = BookSerializers(boks, many=True)
        return Response(serilizer.data)
class BookApiView(APIView):
   
    def get(self, request):
        # print(request.method) # GET,POST,PUT,UPDATE,DELETE
        queryset = Book.objects.all()
        serializer = BookSerializers(queryset, many=True)
        return Response({

            "book":serializer.data
        })

import os
from django.conf import settings
class Downland_ApiView(APIView):
    permission_classes = [AllowAny]
    def get(self,request,pk):
        
        try:
            bok = Book.objects.get(id=int(pk))
        except:
            return Response({'error':'hato'})
        print(bok.file.url)
        file_url = f"{settings.BASE_DIR}{bok.file.url}"
        print(file_url)
        file = open(file_url,'rb')
        short = base64.b64encode(file.read())
        return FileResponse(file,as_attachment=True)
    
    
    
        # serializer = DownlandSerializers(bok, many=False)
        
        # return Response({

        #     # "book":serializer.data,
        #     'short':short
        # })


class ContactApiView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ContactSerializers(data=request.data)
        if serializer.is_valid():
            print(1)
            try:
                student = Student.objects.get(user=request.user)
            except:
                student = None    
            contact = serializer.save(serializer.data,student)
            if contact is None:
                return Response({ "status":"error", "error_status":INVALID_DATA })

            return Response({ "status":"ok" })
        return Response({ "status":"error", "errors":serializer.errors })