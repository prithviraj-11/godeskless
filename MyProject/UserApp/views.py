from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from UserApp.models import User
from UserApp.serializers import UserSerializer
# Create your views here.

@csrf_exempt
def userApi(request,id=0):
    if(request.method=='GET'):
        user_info=User.objects.all()
        user_serializer=UserSerializer(user_info,many=True)
        return JsonResponse(user_serializer.data,safe=False)
    elif(request.method=='POST'):
        user_data=JSONParser().parse(request)
        user_serializer=UserSerializer(data=user_data)
        #print(user_serializer)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False) 
    elif(request.method=='PUT'):
        user_data=JSONParser().parse(request)
        user_info=User.objects.get(userId=user_data['userId'])
        user_serializer=UserSerializer(user_info,data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse("Update Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif(request.method=='DELETE'):
        user_get=User.objects.get(userId=id)
        user_get.delete()
        return JsonResponse("Deleted Successfully",safe=False)
