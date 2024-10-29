from django.urls import path, include

app_name = 'Register_Login'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]



