from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.utils import timezone
from .models import Restaurant, Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, VoteSerializer
from rest_framework.decorators import action
from django.db.models import Count
from rest_framework.exceptions import ValidationError


class RestaurantViewSet(viewsets.ModelViewSet):
    """ViewSet for Restaurant operations."""

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [permissions.IsAuthenticated]


class MenuViewSet(viewsets.ModelViewSet):
    """ViewSet for Menu operations."""

    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Use Django's timezone to get the current day of the week
        current_day = timezone.now().strftime("%A").lower()
        return Menu.objects.filter(day=current_day)


class VoteViewSet(viewsets.ModelViewSet):
    """ViewSet for Vote operations."""

    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        employee = request.user
        menu_id = request.data.get("menu")

        # Validate menu ID
        try:
            menu = Menu.objects.get(pk=menu_id)
        except Menu.DoesNotExist:
            raise ValidationError({"menu": "This menu does not exist."})

        # Check if the employee has already voted for this menu
        if Vote.objects.filter(employee=employee, menu=menu).exists():
            return Response(
                {"detail": "You have already voted for this menu."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create the vote
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(employee=employee, menu=menu)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=["get"])
    def results(self, request):
        # Get the current day
        current_day = timezone.now().strftime("%A").lower()
        # Get menus for the current day with vote counts
        menus = Menu.objects.filter(day=current_day).annotate(vote_count=Count("votes"))
        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)
