from django.urls import path 
from .views import * 
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [ 
     #path('ratings', views.RatingsView.as_view()), 
     path('groups/manager/users', ManagersView.as_view()),
     path('groups/manager/users/<int:pk>',ManagersEditView.as_view()),
     #Endpoints for delivery Crew
     path('groups/delivery-crew/users', DeliveryCrewView.as_view()),
     path('groups/delivery-crew/users/<int:pk>', DeliveryCrewEditView.as_view()),
     #Endopoints for menu-items
     path('menu-items/', MenuItemListView.as_view(), name = 'menu-item-create'),
     path('menu-items-edit/<int:pk>',MenuItemEditView.as_view(), name = 'menu-item-edit'),
     path('menu-items-add/', MenuItemCreateView.as_view()),
     path('category/', CategoryCreateView.as_view(), name='category-create'),
     #Using viewset for filtering and seaching
     path('menu-items-new', MenuItemsViewSet.as_view({'get':'list'})),
     path('menu-items-new/<int:pk>', MenuItemsViewSet.as_view({'get':'retreive'})),
     #path('secret/', secret, name = "secret"),
     #Cats Serializer
     path('cart/', CartListView.as_view()),
     path('cart/<int:pk>', CartEditView.as_view()),
     #Order
     path('orders/', OrderListView.as_view()),
     path('orders/<int:pk>', OrderEditView.as_view()),
     path('orders-add/', OrderCreateView.as_view()),

     path('api-token-auth/', obtain_auth_token),
     path('manager-view/',manager_view),
] 
