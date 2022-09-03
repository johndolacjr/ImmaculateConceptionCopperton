from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from calendarapp.models import Event


class Financial(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    model = Event
    template_name = "financial.html"

class Home(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    model = Event
    template_name = "home.html"

class Social(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    model = Event
    template_name = "social.html"

class Bulletin(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    model = Event
    template_name = "bulletin.html"

class History(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    model = Event
    template_name = "history.html"
    
class DashboardView(LoginRequiredMixin, View):
    login_url = "accounts:signin"
    template_name = "calendarapp/dashboard.html"

    def get(self, request, *args, **kwargs):
        events = Event.objects.get_all_events(user=request.user)
        running_events = Event.objects.get_running_events(user=request.user)
        latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
        context = {
            "total_event": events.count(),
            "running_events": running_events,
            "latest_events": latest_events,
        }
        return render(request, self.template_name, context)
