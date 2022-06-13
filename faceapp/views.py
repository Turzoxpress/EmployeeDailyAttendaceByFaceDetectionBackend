from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

from .models import User

from .config import database_name, userColl



# Create your views here.

class registerNewUser(APIView):
    
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        
        return JsonResponse({"status" : "success", "message" : "Method not allowed"})

    def post(self, request, *args, **kwargs):
        '''
        Create the Todo with given todo data
        '''
        body = request.POST

        employee_id = body['employee_id']
        name = body['name']
        phone = body['phone']
        image_path = ""
        punch_status = ""
        user_type = body['user_type']

        if User.objects.filter(employee_id=employee_id).exists():
            return JsonResponse({"status" : "Success", "message" : "User already exists with this id!"})
   

        dataToSave = User(employee_id = employee_id, name = name, phone = phone, image_path = image_path, punch_status = punch_status, user_type = user_type)
        result = dataToSave.save()
        
        
        
        
        return JsonResponse({"status" : "Success", "message" : "User created successfully", "data" : result})
           
