from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.
from .models import Mahsulot
class HomePageView(ListView):
	model = Mahsulot
	template_name = 'home.html'