from django.shortcuts import render
from . import views

def home(request):
	return render(request, 'sitepages/home.html')

def about_us(request):
	return render(request, 'sitepages/about-us.html')

def our_menu(request):
	return render(request, 'sitepages/our-menu.html')
