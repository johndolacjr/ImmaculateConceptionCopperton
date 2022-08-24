from django.shortcuts import render

# Create your views here.

def calendar2(request):
	return render(request, "main/calendar2.html", {})