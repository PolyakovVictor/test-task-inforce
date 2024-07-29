from rest_framework import serializers

from users.serializers import EmployeeSerializer
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
    employee = EmployeeSerializer(read_only=True)  # Use nested EmployeeSerializer
    menu_details = (
        serializers.SerializerMethodField()
    )  # Add a method field for menu details

    class Meta:
        model = Vote
        fields = ["id", "employee", "menu_details", "created_at"]

    def get_menu_details(self, obj):
        """Get the menu details for the current vote."""
        menu = obj.menu
        return {
            "id": menu.id,
            "restaurant": menu.restaurant.name,
            "items": menu.items,
            "day": menu.day,
        }

    def create(self, validated_data):
        # Set the employee to the authenticated user
        validated_data["employee"] = self.context["request"].user
        return super().create(validated_data)
