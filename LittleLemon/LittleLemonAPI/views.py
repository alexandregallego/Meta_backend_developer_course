from rest_framework import generics
from .models import MenuItem, Category, Order
from .serializers import MenuItemSerializer, CategorySerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields = ['price']
    search_fields = ['category']


class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

    def get_permissions(self):
        if (self.request.method == 'GET'):
            return []

        return [IsAuthenticated()]


class OrdersView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
