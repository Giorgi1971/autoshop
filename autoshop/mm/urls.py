from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)
router.register(r'carts', CartViewSet)
router.register(r'tags', TagViewSet)
router.register(r'cart_items', CartItemViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from . import views


# urlpatterns = [
#     path('', views.api_root),
#
#     path('categories/', views.CategoryViewSet.as_view({
#         'get': 'list',
#         'post': 'create'
#     }),
#          name='category-list'),
#
#     path('categories/<int:pk>/', views.CategoryViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='category-detail'),
#
#     path('products/', views.ProductViewSet.as_view({'get': 'list'}),
#          name='product-list'),
#
#     path('products/<int:pk>/', views.ProductViewSet.as_view({
#         'get': 'retrieve',
#         'put': 'update',
#         'patch': 'partial_update',
#         'delete': 'destroy'
#     }), name='category-detail'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
