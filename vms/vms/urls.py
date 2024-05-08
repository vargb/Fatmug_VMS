"""
URL configuration for vms project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from jwt_auth.views import Login,Logout,Register

urlpatterns = [
    path("auth/", include("jwt_auth.urls")),
    path("auth/token",TokenObtainPairView.as_view()),
    path("auth/refresh",TokenRefreshView.as_view()),
    path("vendors/", include("vendors.urls", namespace="vendors")),
    path("purchase_orders/", include("orders.urls", namespace="orders")),
]
