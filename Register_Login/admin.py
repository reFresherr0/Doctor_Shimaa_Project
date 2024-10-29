from .models import Profile, UserPosition, UserLoginLocation, Volunteer
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from .forms import ImageUploadAdminFormVolunteer

# Register your models here.


class Register(admin.ModelAdmin):
    list_filter = ("email","profile_name", "created")
    list_display = ("email","profile_name",'created','phone_number','is_active','id'
                  )
    search_fields = ['email']
    formfield_overrides = {
        models.ManyToManyField : {'widget' : CheckboxSelectMultiple},
    }


class UserPosition_admin(admin.ModelAdmin):
    list_display = ("position_en",'created',)


class Volunteer_admin(admin.ModelAdmin):
    list_display = ("email",'name','whatsapp','created')
    form = ImageUploadAdminFormVolunteer  # Use the custom form

    def image_tag(self, obj):
        if obj.img:
            return f'<img src="{obj.img.url}" />'
        return "No Image"


class UserLoginLocation_admin(admin.ModelAdmin):
    list_display = ("user",'ip_address','login_time')
    readonly_fields = ('login_time',)



admin.site.register(Profile, Register)
admin.site.register(UserPosition, UserPosition_admin)
admin.site.register(UserLoginLocation, UserLoginLocation_admin)
admin.site.register(Volunteer, Volunteer_admin)

