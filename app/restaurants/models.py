from django.db import models
from django.utils import timezone
from users.models import Employee

DAYS_OF_WEEK = [
    ("monday", "Monday"),
    ("tuesday", "Tuesday"),
    ("wednesday", "Wednesday"),
    ("thursday", "Thursday"),
    ("friday", "Friday"),
    ("saturday", "Saturday"),
    ("sunday", "Sunday"),
]


class Restaurant(models.Model):
    """Model representing a restaurant."""

    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Menu(models.Model):
    """Model representing a menu for a restaurant."""

    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="menus"
    )
    day = models.CharField(max_length=10, choices=DAYS_OF_WEEK)
    items = models.TextField()  # Stores menu items as plain text

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("restaurant", "day")
        ordering = ["restaurant", "day"]

    def __str__(self):
        return f"{self.restaurant.name} - {self.day.capitalize()}"


class Vote(models.Model):
    """Model representing a vote by an employee for a menu."""

    employee = models.ForeignKey(
        Employee, on_delete=models.CASCADE, related_name="votes"
    )
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("employee", "menu")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.employee.username} voted for {self.menu.restaurant.name} on {self.menu.day}"
