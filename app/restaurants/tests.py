from django.test import TestCase
from .models import Restaurant, Menu, Vote
from users.models import Employee
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer


class RestaurantSerializerTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )
        self.serializer = RestaurantSerializer(instance=self.restaurant)

    def test_restaurant_serializer(self):
        data = self.serializer.data
        self.assertEqual(data["name"], "Test Restaurant")
        self.assertEqual(data["address"], "123 Test St")


class MenuSerializerTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )
        self.menu = Menu.objects.create(
            restaurant=self.restaurant, day="monday", items="Pizza, Pasta, Salad"
        )
        self.serializer = MenuSerializer(instance=self.menu)

    def test_menu_serializer(self):
        data = self.serializer.data
        self.assertEqual(data["restaurant_name"], "Test Restaurant")
        self.assertEqual(data["day"], "monday")
        self.assertEqual(data["items"], "Pizza, Pasta, Salad")


class VoteSerializerTest(TestCase):
    def setUp(self):
        self.employee = Employee.objects.create_user(
            username="testuser", first_name="John", last_name="Doe", password="password"
        )
        self.restaurant = Restaurant.objects.create(
            name="Test Restaurant", address="123 Test St"
        )
        self.menu = Menu.objects.create(
            restaurant=self.restaurant, day="monday", items="Pizza, Pasta, Salad"
        )
        self.vote = Vote.objects.create(employee=self.employee, menu=self.menu)
        self.serializer = VoteSerializer(instance=self.vote)

    def test_vote_serializer(self):
        data = self.serializer.data
        self.assertEqual(data["employee"]["first_name"], "John")
        self.assertEqual(data["menu_details"]["restaurant"], "Test Restaurant")
        self.assertEqual(data["menu_details"]["items"], "Pizza, Pasta, Salad")
