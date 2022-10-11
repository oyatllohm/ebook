from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from django.http import JsonResponse
from .error_status import *
from rest_framework.authtoken.models import Token
# Create your views here.

class RegisterApiView(APIView):
    def post(self, request):
        serializer = StudentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status":"success"
            })

        return Response({
                "status":"error",
                "errors":serializer.errors
            })
        
    
class Autoview(APIView):
    def post(self,request):
        passport = request.data.get('passport')
        if passport is None:
            return Response({
                'Error_status':PASSPORT_NUMBER_NOD_SEND,
                'status':'Error'
            })

        try:
            user = User.objects.get(username=passport)
        except:
            return Response({'Error_status':USER_NOT_FOUND,
                'status':'Error'})
        token = Token.objects.create(user=user)
        return Response({'Error_status':SUCCESS,
                'status':'ok',
                'token': token.key})

from .load_data import load_data
def LoadView(request):
    students = load_data()
    print(students)
    # user = User.objects.all().delete()
    # user = Student.objects.all().delete()
    exists = 0
    create = 0
    for s in students:
        passport = s['passport']
        try:
            user = User.objects.get(username=passport)
        except:
            user = User.objects.create(username=passport,password=passport)

        faculty = Faculty.objects.get_or_create(title=s['faculty'])[0]
        try:
            student = Student.objects.get(user=user)
            exists += 1
        except:    
            student = Student.objects.create(
                user=user,
                name=s['name'],
                surname=s['surname'],
                middlename=s['middlename'],
                pinfl=s['pinfl'],
                passport=s['passport'],
                course=s['course'],
                group=s['group'],
                faculty=faculty
                )
            create += 1
        print("Created ", create)
        print("Exists ", exists)
    return JsonResponse({
        "create":create,
        "exists":exists,

    })

