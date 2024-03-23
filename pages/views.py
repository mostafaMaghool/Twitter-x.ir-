from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

#def home_page(request):
#   return render(request, "home.html",{})

class HomePageView(TemplateView):
    template_name= 'home.html'

class aboutPageView(TemplateView):
    template_name= 'about.html'
