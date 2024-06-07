#from .views import AboutPageView, HomePageView
from django.urls import path
from . import views

# urlpatterns = [
#     path('', HomePageView.as_view(), name='home'),  # Route für die Homepage
#     path('about/', AboutPageView.as_view(), name='about'),  # Route für die About-Seite
# ]

urlpatterns = [
    path('', views.home, name='home'),  # Route für die Homepage
    path('about/', views.about, name='about'),  # Route für die About-Seite
]