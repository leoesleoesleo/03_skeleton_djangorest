# Django
from rest_framework import serializers
from integration.component2.models import Orders


class OutputOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'