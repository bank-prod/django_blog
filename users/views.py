from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
	if request.method =='POST' :
		print('OK')
	form= UserCreationForm()
	return render(request,'pages/register.html', {'form':form})