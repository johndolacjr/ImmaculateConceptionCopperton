from django.shortcuts import render

# Create your views here.

def financial(request):
	return render(request, "main/financial.html", {})