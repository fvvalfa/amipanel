from django.shortcuts import render, HttpResponse
# from home.models import *
from django.contrib import messages
# from blog.models import Post
from django.shortcuts import redirect




def show_home_page(request):
    
	
	return render(request,"home/home.html")
