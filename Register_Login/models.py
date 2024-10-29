from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager




class UserManager(BaseUserManager):
    def get_by_natural_key(self, username):
        """
        To make email login case sensetive.
        """
        
        return self.get(email__iexact=username)

    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        
        if not email:
            raise ValueError('Email does not included!')
        
        email = self.normalize_email(email)
        user = self.model(email=email, password=password, **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        
        return self.create_user(email=email, password=password, **extra_fields)


class UserPosition(models.Model):
    position_en = models.CharField(max_length=50, null=True)
    position_ar = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now=True)


    objects = UserManager()

    def __str__(self):
        return self.position_en


class Profile(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name='email', unique=True)
    profile_name = models.CharField(max_length=50, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    image = models.ImageField(upload_to="Profile", blank=True,null = True )
    phone_number =  models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now=True)
    Position = models.ForeignKey(UserPosition, on_delete=models.CASCADE,blank=True,null = True,)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return self.email

  
class Volunteer(models.Model):
    email = models.EmailField(verbose_name='email', unique=True)
    name = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to="Volunteers", blank=True,null = True )
    phone_number =  models.CharField(max_length=40, null=True)
    whatsapp =  models.CharField(max_length=40, null=True)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.email


class UserLoginLocation(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,blank=True,null = True,)
    ip_address =  models.CharField(max_length=40, null=True)
    login_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.user.email)