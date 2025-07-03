from rest_framework import generics, permissions, filters
from rest_framework.response import Response
from django.contrib.auth.models import User, Group
from .models import Category, MenuItem, Cart, Order, OrderItem
from .serializers import CategorySerializer, MenuItemSerializer, CartSerializer, OrderSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.db.models import Sum
from rest_framework.pagination import PageNumberPagination

# Admin: Assign users to Manager group
class ManagerGroupView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

    def post(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        manager_group = Group.objects.get(name='Manager')
        user.groups.add(manager_group)
        return Response({'message': 'User added to Manager group'})

# Admin: Access Manager group
class ManagerGroupListView(generics.ListAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]

# Admin: Add Menu Items
class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAdminUser]

# Admin: Add Categories
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

# Managers: Update Item of the Day
class ItemOfTheDayView(generics.UpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MenuItem.objects.all() if self.request.user.groups.filter(name='Manager').exists() else MenuItem.objects.none()

    def patch(self, request, *args, **kwargs):
        MenuItem.objects.update(is_item_of_the_day=False)  # Reset all
        return super().patch(request, *args, **kwargs)

# Managers: Assign users to DeliveryCrew
class DeliveryCrewAssignView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='DeliveryCrew')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(groups__name='DeliveryCrew') if self.request.user.groups.filter(name='Manager').exists() else User.objects.none()

    def post(self, request):
        user_id = request.data.get('user_id')
        user = User.objects.get(id=user_id)
        delivery_group = Group.objects.get(name='DeliveryCrew')
        user.groups.add(delivery_group)
        return Response({'message': 'User added to DeliveryCrew group'})

# Managers: Assign orders to DeliveryCrew
class OrderAssignView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.all() if self.request.user.groups.filter(name='Manager').exists() else Order.objects.none()

# DeliveryCrew: Access assigned orders
class DeliveryCrewOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(delivery_crew=self.request.user)

# DeliveryCrew: Update order as delivered
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(delivery_crew=self.request.user)

# Customers: Browse all categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

# Customers: Browse all menu items
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['price']
    search_fields = ['category__name']
    pagination_class = PageNumberPagination

# Customers: Add to cart
class CartCreateView(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Customers: Access cart
class CartListView(generics.ListAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

# Customers: Place orders
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart_items = Cart.objects.filter(user=self.request.user)
        total = sum(item.menu_item.price * item.quantity for item in cart_items) or 0
        order = serializer.save(user=self.request.user, total=total)
        for item in cart_items:
            OrderItem.objects.create(order=order, menu_item=item.menu_item, quantity=item.quantity)
        cart_items.delete()

# Customers: Browse their own orders
class CustomerOrdersView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)