"""
URL configuration for VividComm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include # Import include
# from rest_framework.authtoken import views as auth_views_drf # Optional: If you want DRF's default token endpoint

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')), # Our user-related URLs
    # If you ever want DRF's default token endpoint (less common when you custom implement login/logout):
    # path('api-token-auth/', auth_views_drf.obtain_auth_token),
]