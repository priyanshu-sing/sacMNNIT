from django.shortcuts import render

# Create your views here.

def avishkar(request):
	return render(request,'Technical/avishkar.html', {})
	
def technological(request):
	return render(request,'Technical/technological.html', {})

def hack36(request):
	return render(request,'Technical/hack36.html', {})

def prosang(request):
	return render(request,'Technical/prosang.html', {})