from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse

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

        name = body['name']
        phone = body['phone']
        #image_path = body['image_path']
        #punch_status = body['punch_status']
        user_type = body['user_type']
        
        
        
        
        
        
        return JsonResponse({"status" : "Success", "data" : name})
           
