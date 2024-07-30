from django.core.management.base import BaseCommand
from django.utils import timezone
from users.models import Employee
from restaurants.models import Restaurant, Menu, Vote
import random


class Command(BaseCommand):
    help = "Creates test data for the lunch decision app"

    def handle(self, *args, **kwargs):
        self.stdout.write("Creating test data...")

        # Create restaurants
        restaurants = []
        for i in range(5):
            restaurant = Restaurant.objects.create(
                name=f"Restaurant {i+1}", address=f"{i+1} Main St, City"
            )
            restaurants.append(restaurant)

        self.stdout.write(self.style.SUCCESS(f"Created {len(restaurants)} restaurants"))

        # Create menus
        menus = []
        today = timezone.now().date()
        for restaurant in restaurants:
            for i in range(7):  # Create menus for a week
                menu = Menu.objects.create(
                    restaurant=restaurant,
                    day=[
                        "monday",
                        "tuesday",
                        "wednesday",
                        "thursday",
                        "friday",
                        "saturday",
                        "sunday",
                    ][i % 7],
                    items=f"Dish {i+1} and Side {i+1}",
                )
                menus.append(menu)

        self.stdout.write(self.style.SUCCESS(f"Created {len(menus)} menus"))

        # Create employees
        employees = []
        for i in range(20):
            employee = Employee.objects.create(
                username=f"employee{i+1}",
                email=f"employee{i+1}@example.com",
                password="testpass123",
            )
            employees.append(employee)

        self.stdout.write(self.style.SUCCESS(f"Created {len(employees)} employees"))

        # Create votes
        votes = []
        for employee in employees:
            # Each employee votes for a random menu for today
            todays_menu = random.choice(
                [
                    menu
                    for menu in menus
                    if menu.day == timezone.now().strftime("%A").lower()
                ]
            )
            vote = Vote.objects.create(employee=employee, menu=todays_menu)
            votes.append(vote)

        self.stdout.write(self.style.SUCCESS(f"Created {len(votes)} votes"))

        self.stdout.write(self.style.SUCCESS("Test data creation completed"))
