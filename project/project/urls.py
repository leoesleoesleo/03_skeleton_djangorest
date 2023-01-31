# Django
from django.conf import settings

from django.contrib import admin
from django.urls import include, path
"""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
"""

urlpatterns = [
    path(
        'component2/',
        include('integration.component2.urls')
    )
]
