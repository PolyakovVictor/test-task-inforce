from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class Employee(AbstractUser):
    """Custom user model for employees."""

    email = models.EmailField(unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name="employee_set",  # Change this
        blank=True,
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name="groups",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="employee_user_set",  # Change this
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
