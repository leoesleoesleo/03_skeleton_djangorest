# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.views import TokenObtainPairView

# Internal

logger = logging.getLogger(__name__)

