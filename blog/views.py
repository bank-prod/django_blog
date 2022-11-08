from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def home(request):
	posts = Post.objects.all()
	context = { 'posts':posts}
	return render(request,"pages/home.html",context)

def about(request):
	return render(request,"pages/about.html")