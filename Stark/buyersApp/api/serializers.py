from rest_framework import serializers
from buyersApp.models import Buyers


class BuyersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyers
        fields="__all__"


class LoginOtpSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyers
        fields=["buyers_number"]
