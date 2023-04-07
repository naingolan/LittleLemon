from django.shortcuts import get_object_or_404, render
from .models import *
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *


from rest_framework.permissions import *
from rest_framework.decorators import *
from rest_framework.response import *
from rest_framework.authentication import *
from django.contrib.auth.models import User, Group
from django.http import *
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .permissions import *

#This is to List all items
@permission_classes([IsAuthenticated])
class MenuItemListView(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

#This is to Edit and Delete Items
@permission_classes([IsManagerUser])
class MenuItemEditView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

#This is to Post a new Item
@permission_classes([IsManagerUser])
class MenuItemCreateView(generics.CreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
# Create your views here.
# class RatingsView(generics.ListCreateAPIView):
#     queryset = Rating.objects.all()
#     serializer_class = RatingSerializer

#     def get_permissions(self):
#         if(self.request.method == 'GET'):
#             return []
#         return [IsAuthenticated()]

from .serializers import *
class ManagersView(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        managers_group = Group.objects.get(name='Manager')
        return managers_group.user_set.all()
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        if username:
            user = User.objects.filter(username=username).first()
            if user:
                managers_group = Group.objects.get(name='Manager')
                managers_group.user_set.add(user)
                return Response({"messages": "User added to Manager group."}, status=status.HTTP_200_OK)
            else:
                return Response({"messages": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"messages": "Username is required."}, status=status.HTTP_400_BAD_REQUEST)


class ManagersEditView(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        managers_group = Group.objects.get(name='Manager')
        return managers_group.user_set.all()


#This is for Delivery Group   
@permission_classes([IsAdminUser])
@permission_classes([IsManagerUser])
class DeliveryCrewView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    def get_queryset(self):
        delivery_crew = Group.objects.get(name='Delivery Crew')
        return delivery_crew.user_set.all()

class DeliveryCrewEditView(generics.DestroyAPIView, generics.RetrieveAPIView):
    permission_classes = [IsManagerUser]
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer

    def get_queryset(self):
        managers_group = Group.objects.get(name='Delivery Crew')
        return managers_group.user_set.all()

@permission_classes([IsAuthenticated])
class CartListView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartListView(generics.RetrieveAPIView, generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

@api_view()
@permission_classes([IsAdminUser])
def manager_view(request):
    if request.user.groups.filter(name="Delivery Crew").exists():
        return Response({"Message": "Only Manager Should See this"})
    else:
        return Response({"Message":"Your are not authorized"}, 403)