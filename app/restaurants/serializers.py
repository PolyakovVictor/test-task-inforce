from rest_framework import serializers
from .models import Restaurant, Menu, Vote


class MenuSerializer(serializers.ModelSerializer):
    votes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    restaurant_name = serializers.CharField(source="restaurant.name", read_only=True)

    class Meta:
        model = Menu
        fields = [
            "id",
            "restaurant",
            "restaurant_name",
            "day",
            "items",
            "created_at",
            "updated_at",
            "votes",
        ]


class RestaurantSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True, read_only=True)

    class Meta:
        model = Restaurant
        fields = ["id", "name", "address", "menus"]


class VoteSerializer(serializers.ModelSerializer):
    employee = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Vote
        fields = ["id", "employee", "menu", "created_at"]

    def create(self, validated_data):
        # Set the employee to the authenticated user
        validated_data["employee"] = self.context["request"].user
        return super().create(validated_data)
