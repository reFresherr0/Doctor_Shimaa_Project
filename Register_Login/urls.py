from django.urls import path,re_path
from django.contrib.auth import views as auth_views
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'Register_Login'

urlpatterns = [
    # APIs URL
    path('create_users_API/', view= views.create_users_API.as_view(), name='create_users_API'),
    path('login_view/', view= views.LoginView, name='login_view'),
    path('get_active_users/', view= views.get_active_users.as_view(), name='get_active_users'),


]



