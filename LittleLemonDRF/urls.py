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
     path('category/', CategoryCreateView.as_view(), name='category-create'),
     #path('secret/', secret, name = "secret"),
     #Cats Serializer
     path('cart/', CartListView.as_view()),
     path('cart/<int:pk>', CartListView.as_view()),
     path('api-token-auth/', obtain_auth_token),
     path('manager-view/',manager_view),
] 
