from rest_framework import authentication, generics, mixins, permissions
from .models import MenuItem, Category, Order
from .serializers import MenuItemSerializer, CategorySerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    search_fields = ['category']


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [permissions.DjangoModelPermissions]


class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.DjangoModelPermissions]
