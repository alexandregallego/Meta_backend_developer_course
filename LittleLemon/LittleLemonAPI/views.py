from rest_framework import generics, permissions
from .models import MenuItem, Order
from .serializers import MenuItemSerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    search_fields = ['category']
    permission_classes = [IsAuthenticatedOrReadOnly]


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class ManagersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name="Managers")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class SingleManagersView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name="Managers")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name="Delivery crew")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]


class SingleDeliveryCrewView(generics.DestroyAPIView):
    queryset = User.objects.filter(groups__name="Delivery crew")
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
