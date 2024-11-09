# Project_45_3/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('personal_site.urls')),  # Include personal_site app's URLs
]
