from django.shortcuts import render

# Create your views here.

def social(request):
	return render(request, "main/social.html", {})