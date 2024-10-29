from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import CustomUserManager



class UserPosition(models.Model):
    position_en = models.CharField(max_length=50, null=True)
    position_ar = models.CharField(max_length=50, null=True)
    created = models.DateTimeField(auto_now=True)


    objects = CustomUserManager()

    def __str__(self):
        return self.position_en


class Profile(AbstractBaseUser,PermissionsMixin):

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    GENDER_CHOICES= (
        ('M','Male'),
        ('F','Female'),
    )

    email = models.EmailField(verbose_name='email', unique=True)
    profile_name = models.CharField(max_length=50, null=True)
    img = models.ImageField(upload_to="Profile", blank=True, null = True)
    phone_number =  models.CharField(max_length=20, null=True)
    gender = models.CharField(max_length=1,null=True,blank=True,choices=GENDER_CHOICES)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    Position = models.ForeignKey(UserPosition, on_delete=models.CASCADE,blank=True,null = True,)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_superuser']

    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )


    objects = CustomUserManager()

    def __str__(self) -> str:
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