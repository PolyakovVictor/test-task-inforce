from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Employee
        fields = ["id", "username", "email", "password", "first_name", "last_name"]

    def create(self, validated_data):
        # Hash the password before saving the user
        validated_data["password"] = make_password(validated_data["password"])
        return super(EmployeeSerializer, self).create(validated_data)

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
