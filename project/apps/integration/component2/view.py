# Standard Library
import logging

# Django
from django.core.exceptions import ValidationError
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Internal
#from integration.component2 import services
#from integration.component2.models import Orders
#from integration.component2.serializers import OutputOrdersSerializer

logger = logging.getLogger(__name__)

