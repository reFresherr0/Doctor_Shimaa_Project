from django import forms
from django.core.files.base import ContentFile
import requests
from .models import Volunteer
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import Profile


class ImageUploadAdminFormVolunteer(forms.ModelForm):
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        model = Volunteer
        fields = ['email', 'name', 'phone_number', 'whatsapp', 'img',]  # Display fields in the admin

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Check if image_url is provided
        image_url = self.cleaned_data.get('image_url')
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Get the image name from the URL and save it to the model
                image_name = image_url.split("/")[-1]
                instance.img.save(image_name, ContentFile(response.content), save=False)

        if commit:
            instance.save()
        return instance


class CustomUserCreationForm(UserCreationForm):
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        model = Profile
        fields = ('email', 'profile_name', 'phone_number', 'gender', 'Position', 'is_staff', 'is_active', 'img', 'date_joined',)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Check if image_url is provided
        image_url = self.cleaned_data.get('image_url')
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Get the image name from the URL and save it to the model
                image_name = image_url.split("/")[-1]
                instance.img.save(image_name, ContentFile(response.content), save=False)
        if commit:
            instance.save()
        return instance


class CustomUserChangeForm(UserChangeForm):
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        model = Profile
        fields = ('email', 'profile_name', 'phone_number', 'gender', 'Position', 'is_staff', 'is_active', 'img', 'date_joined',)

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Check if image_url is provided
        image_url = self.cleaned_data.get('image_url')
        if image_url:
            response = requests.get(image_url)
            if response.status_code == 200:
                # Get the image name from the URL and save it to the model
                image_name = image_url.split("/")[-1]
                instance.img.save(image_name, ContentFile(response.content), save=False)

        if commit:
            instance.save()
        return instance
    


class CustomAuthenticationForm(AuthenticationForm):
    pass