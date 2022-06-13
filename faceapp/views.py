from email import utils
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.core.files.storage import default_storage

import os


from .models import User

from .utils.utils import Utils



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
        
        
        user_type = body['user_type']

        if User.objects.filter(employee_id=employee_id).exists():
            return JsonResponse({"status" : "Success", "message" : "User already exists with this id!"})

        
        
        #  Saving POST'ed file to storage
        
        file = request.FILES['photo']
        base = os.path.splitext(file.name)
        fileExt = base[1]
        fileName = Utils.getSystemTimeInMilisecondsString() +   str(fileExt)
        completeName = os.path.join("uploads", fileName)
        Utils.handle_uploaded_file(file, completeName)
        #file_name = default_storage.save(file.name, file)

        image_path = fileName
        punch_status = "No"
   

        dataToSave = User(employee_id = employee_id, name = name, phone = phone, image_path = image_path, punch_status = punch_status, user_type = user_type)
        result = dataToSave.save()
        
        
        
        
        return JsonResponse({"status" : "Success", "message" : "User created successfully", "data" : result})
           
