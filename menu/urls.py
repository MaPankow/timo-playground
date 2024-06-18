from django.urls import path
from . import views
from .views import MenuList

urlpatterns = [
    path('', views.menu, name='menu'),
    path('api/', MenuList.as_view(), name='menu-list'),
]