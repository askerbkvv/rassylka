from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClientViewSet, LinksViewSet, MessageViewSet

app_name = 'rassylka'

router_v1 = DefaultRouter()
router_v1.register('client', ClientViewSet)
router_v1.register('links', LinksViewSet)
router_v1.register('messages', MessageViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls))
]


















# from django.urls import path
# from .views import *
# from rassylka import views
#
# app_name = 'rassylka'
#
# urlpatterns = [
#     path('create-client/', views.apiCreateClient, name="create-client"),
#     path('update-client/<int:pk>/', views.apiUpdateClient, name="update-client"),
#     path('delete-client/<int:pk>/', views.apiDeleteClient, name="delete-client"),
#     path('create-link/', views.apiCreateLink, name="create-link"),
#     path('link-detail/<int:pk>/', views.apiLinkDetails, name="link-detail"),
#     path('update-link/<int:pk>/', views.apiUpdateLink, name="update-link"),
#     path('delete-link/<int:pk>/', views.apiDeleteLink, name="delete-link"),
# ]
#
# # urlpatterns = [
# #     path('link/', views.LinkListView.as_view(), name='link_detail'),
# #     path('link/UD/<int:pk>/', views.LinkUDView.as_view(), name='update_delete_link'),
# #     path('client/', views.ClientListView.as_view(), name='link_detail'),
# #     path('type/UD/<int:pk>/', views.ClientUDView.as_view(), name='update_delete_client'),
# # ]
#
