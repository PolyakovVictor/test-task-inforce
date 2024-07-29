from rest_framework import serializers
from .models import Restaurant, Menu, Vote


class MenuSerializer(serializers.ModelSerializer):
    votes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = [
            "id",
            "restaurant",
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
    class Meta:
        model = Vote
        fields = ["id", "employee", "menu", "created_at"]
