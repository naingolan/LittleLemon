

from django.urls import path
from . import views

urlpatterns = [
    path('managers/', views.ManagerGroupView.as_view(), name='manager-group'),
    path('managers/list/', views.ManagerGroupListView.as_view(), name='manager-list'),
    path('menu-items/', views.MenuItemCreateView.as_view(), name='menu-item-create'),
    path('categories/', views.CategoryCreateView.as_view(), name='category-create'),
    path('item-of-the-day/<int:pk>/', views.ItemOfTheDayView.as_view(), name='item-of-the-day'),
    path('delivery-crew/', views.DeliveryCrewAssignView.as_view(), name='delivery-crew-assign'),
    path('orders/assign/<int:pk>/', views.OrderAssignView.as_view(), name='order-assign'),
    path('delivery-orders/', views.DeliveryCrewOrdersView.as_view(), name='delivery-orders'),
    path('orders/status/<int:pk>/', views.OrderStatusUpdateView.as_view(), name='order-status'),
    path('categories/list/', views.CategoryListView.as_view(), name='category-list'),
    path('menu-items/list/', views.MenuItemListView.as_view(), name='menu-item-list'),
    path('cart/', views.CartCreateView.as_view(), name='cart-create'),
    path('cart/list/', views.CartListView.as_view(), name='cart-list'),
    path('orders/', views.OrderCreateView.as_view(), name='order-create'),
    path('orders/list/', views.CustomerOrdersView.as_view(), name='customer-orders'),
]