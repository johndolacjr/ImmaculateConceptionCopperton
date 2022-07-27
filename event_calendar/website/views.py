from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

# from django.views.generic import View
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render

# from calendarapp.models import Event


# class DashboardView(LoginRequiredMixin, View):
#     login_url = "accounts:signin"
#     template_name = "ImmaculateConceptionCopperton/event_calendar/templates/calendarapp/dashboard.html"

#     def get(self, request, *args, **kwargs):
#         events = Event.objects.get_all_events(user=request.user)
#         running_events = Event.objects.get_running_events(user=request.user)
#         latest_events = Event.objects.filter(user=request.user).order_by("-id")[:10]
#         context = {
#             "total_event": events.count(),
#             "running_events": running_events,
#             "latest_events": latest_events,
#         }
#         return render(request, self.template_name, context)


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/calendar')
def calendar():
    return render_template("calendar.html", user=current_user)

@views.route('ImmaculateConceptionCopperton/event_calendar/templates/calendarapp/dashboard')
def dashboard():
    return render_template("dashboard.html", user=current_user)

@views.route('/history')
def history():
    return render_template("history.html", user=current_user)

@views.route('/financial')
def financial():
    return render_template("financial.html", user=current_user)

@views.route('/social')
def social():
    return render_template("social.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
