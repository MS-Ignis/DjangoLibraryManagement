from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.

# def index(request):
#     return HttpResponse("hi, this is the library home page")

class IndexView(generic.TemplateView):
    template_name = 'index.html'