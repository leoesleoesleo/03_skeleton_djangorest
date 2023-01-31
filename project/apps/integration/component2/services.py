# Standard Library
import logging
from datetime import datetime, timedelta
from typing import Dict, Union
import random

# Django
from django.db import transaction
from django.db.models import QuerySet

# Internal
from integration.component2.models import Orders

logger = logging.getLogger(__name__)


def test_services(
    *,
    dispatcher_id: int
) -> 'QuerySet[Orders]':
    response = Orders.objects.filter(
        pk=dispatcher_id
    ).last()
    return response
