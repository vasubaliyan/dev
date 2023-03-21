from rest_framework import serializers
from accountApp.models import Account


class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model=Account
        fields="__all__"



class ChangePasswordSerializer(serializers.Serializer):
    old_password=serializers.CharField(max_length=20)
    password=serializers.CharField(max_length=20)
    confirm_password=serializers.CharField(max_length=20)


def validation(attrs):
    if attrs["password"] !=attrs["confirm_password"]:
        raise serializers.ValidationError({"password":"password not match"})
    return attrs
