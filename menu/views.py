from django.shortcuts import render
from .models import MenuCategory, MenuItem
from rest_framework import generics
from .serializers import MenuCategorySerializer, MenuItemSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

def menu(request):
    categories = MenuCategory.objects.all()
    return render(request, 'menu/menu.html', {'categories': categories})

class MenuList(generics.ListAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing the menu items.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer