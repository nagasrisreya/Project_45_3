# urls.py

from django.contrib import admin
from django.urls import path
from . import views  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page
    path('resume/', views.resume, name='resume'),  # Resume page
]
