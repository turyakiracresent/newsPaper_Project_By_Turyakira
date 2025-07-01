from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def newsView (request):
#     return HttpResponse("<h1>Hello, World !</h1>")

# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = 'index.html'  # Path to your HTML template

# class AboutPageView(TemplateView):
#     template_name = 'about.html'  # Path to your HTML template
    
from django.views.generic import TemplateView

from django.views.generic import ListView

from .models import Post    

class HomePageView(ListView):
    model = Post

    template_name = 'index.html'  # Template File to render this view



class AboutPageView(ListView):
    model = Post

    template_name = 'about.html'  # Template File to render this view


   