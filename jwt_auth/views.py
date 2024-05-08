from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from .models import User
from rest_framework.exceptions import AuthenticationFailed
import datetime,jwt

# Create your views here.
class Register(APIView):
    def post(self,request):
        serializer=UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    
class Login(APIView):
    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        payload={
            "id":password,
            "exp":datetime.datetime.now()+datetime.timedelta(minutes=5),
            "iat":datetime.datetime.now()
        }
        
        token =jwt.encode(payload,'secret',algorithm="HS256")
        
        user=User.objects.filter(username=username).first()
        
        if user is None:
            raise AuthenticationFailed("authentication failed")
        
        if user.password!=password:
            raise AuthenticationFailed("incorrect password")
        
        resp=Response({"login":"successfull","token":token})
        resp.set_cookie(key="token",value=token,httponly=True)
        return resp
        
class Logout(APIView):
    def post(self,request):
        resp=Response()
        resp.delete_cookie("token")
        resp.data={
            "logout":"successfull"
        }
        return resp