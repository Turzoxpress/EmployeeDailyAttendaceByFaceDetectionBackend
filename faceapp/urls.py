from django.urls import path
from faceapp import views

urlpatterns = [
    path('registerNewUser', views.registerNewUser.as_view()),
]
