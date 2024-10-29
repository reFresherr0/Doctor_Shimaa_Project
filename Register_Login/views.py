from django.contrib.auth import authenticate, login as user_login
from django.utils.translation import gettext as _
from django.contrib.auth.models import update_last_login
from django.views.decorators.csrf import csrf_protect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer, UserSerializer
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Profile



class create_users_API(APIView):
    def post(self,request,):
        serializer = UserSerializer(data= request.data,partial=True)
        if serializer.is_valid():
            user = Profile.objects.create_user(
                    email=request.data['email'],
                    first_name=request.data['first_name'],
                    last_name=request.data['last_name'],
                    password=request.data['password'],
                    city=serializer.validated_data['city'],
                    phone_number=request.data['phone_number'],
                    is_active = True,
                )
            if user:
                return Response("User Created Successfully", status = status.HTTP_200_OK)
            else:
                return Response("Error Creating User", status = status.HTTP_403_FORBIDDEN)
        else:
            return Response("Serializer Not Valid", status = status.HTTP_403_FORBIDDEN)
        
    def get_serializer(self):
        return UserSerializer()

# Get All Users
class get_active_users(GenericAPIView):
    def get(self,request):
        all = Profile.objects.filter(is_active = True)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=False)
    
    def get_serializer(self):
        return UserSerializer()


# Login Users

user_response = openapi.Response('response description', UserSerializer)

@csrf_protect
@swagger_auto_schema(method='get', responses={200: user_response})
@swagger_auto_schema(method='post', request_body=LoginSerializer)
@api_view(['POST','GET',])
def LoginView(request):
    if request.method == 'POST':
        serializer = LoginSerializer(data=request.data, context={'request': request})

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']

            user = authenticate(request, email=email, password=password)

            if user is not None:
                if user.is_active:
                    update_last_login(None, user)
                    user_login(request, user)
                    return Response({"message": "Login successful","Names" : serializer.data,"code":status.HTTP_200_OK}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "User account is not active","code":status.HTTP_403_FORBIDDEN}, status=status.HTTP_403_FORBIDDEN)
            else:
                return Response({"message": "Invalid credentials","code":status.HTTP_403_FORBIDDEN}, status=status.HTTP_403_FORBIDDEN)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        

    if request.method == 'GET':
        all = Profile.objects.filter(is_active = True,)
        serializer = UserSerializer(all,many = True)
        return JsonResponse({"Names": serializer.data}, safe=True,status = status.HTTP_200_OK)