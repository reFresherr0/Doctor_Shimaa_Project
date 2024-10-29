from .models import Profile, UserPosition, UserLoginLocation, Volunteer
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from .forms import ImageUploadAdminFormVolunteer, CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

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
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True  # Allow HTML tags in admin for image preview



class UserLoginLocation_admin(admin.ModelAdmin):
    list_display = ("user",'ip_address','login_time')
    readonly_fields = ('login_time',)


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Profile
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Personal Information'), {'fields': ('profile_name', 'phone_number', 'Position', 'img', 'image_url')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',  'profile_name', 'phone_number', 'Position', 'img', 'image_url', 'password1', 'password2', 'is_staff', 'is_active',)}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


    def image_tag(self, obj):
        if obj.img:
            return f'<img src="{obj.img.url}" />'
        return "No Image"
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True  # Allow HTML tags in admin for image preview

    




admin.site.register(Profile, CustomUserAdmin)
admin.site.register(UserPosition, UserPosition_admin)
admin.site.register(UserLoginLocation, UserLoginLocation_admin)
admin.site.register(Volunteer, Volunteer_admin)

