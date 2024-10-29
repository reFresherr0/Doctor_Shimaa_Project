from django import forms
from django.core.files.base import ContentFile
import requests
from .models import Article, Book



class ImageUploadAdminFormArticle(forms.ModelForm):
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        model = Article
        fields = ['english_title', 'arabic_title', 'category', 
                'subcategory', 'description', 'img_description', 'description', 'content', 'reviewer_id', 'img',]  # Display fields in the admin


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
    

class ImageUploadAdminFormBook(forms.ModelForm):
    image_url = forms.URLField(label="Image URL", required=False)

    class Meta:
        model = Book
        fields = ['title', 'description', 'downloading_link', 'img',]  # Display fields in the admin

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