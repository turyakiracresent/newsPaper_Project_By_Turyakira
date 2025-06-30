from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# def newsView (request):
#     return HttpResponse("<h1>Hello, World !</h1>")

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'index.html'  # Path to your HTML template

class AboutPageView(TemplateView):
    template_name = 'about.html'  # Path to your HTML template
    