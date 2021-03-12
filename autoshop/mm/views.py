from .models import *
from .permissions import IsOwnerOrReadOnly
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from .permissions import *
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import action


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('order')
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsSuperUserOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def slug(self, request, *args, **kwargs):
        product = self.get_object()
        return Response(product.slug)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    # def get(self, request, *args, **kwargs):
    #     product = self.get_object()
    #     return Response(product.slug)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all().order_by('cart')
    serializer_class = CartItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, HaveCart]


class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class SnippetViewSet(viewsets.ModelViewSet):
#     """
#     This viewset automatically provides `list`, `create`, `retrieve`,
#     `update` and `destroy` actions.
#
#     Additionally we also provide an extra `highlight` action.
#     """
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsOwnerOrReadOnly]
#
#     @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
#     def highlight(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
