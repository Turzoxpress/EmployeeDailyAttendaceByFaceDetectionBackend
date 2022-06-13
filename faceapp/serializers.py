from rest_framework import serializers
from .models import User
class UserSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = User
        fields = ( 'name', 'phone', 'image_path','punch_status', 'user_type')