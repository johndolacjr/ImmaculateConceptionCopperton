from django.shortcuts import render

# Create your views here.

def bulletin(request):
	return render(request, "main/bulletin.html", {})