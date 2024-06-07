from django.http import HttpResponse
from django.shortcuts import render
#from django.views.generic import TemplateView

# def home(request):
#   return HttpResponse("<h1> Hello, world. You're at the home page. </h1>")

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


# class HomePageView(TemplateView):
#     template_name = "home.html"

# class AboutPageView(TemplateView):
#     template_name = "about.html"
