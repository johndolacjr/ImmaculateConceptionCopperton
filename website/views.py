# from flask import Flask, render_template
# from flask_fontawesome import FontAwesome
from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json
# import fontawesome as fa

# print(fa.icons['thumbs-up'])

# app = Flask(__name__)
# fa = FontAwesome(app)
# app.run(host='127.0.0.1:5000', port=8080)

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

# @views.route('/base.html')
# def base():
#     return render_template('base.html', user=current_user)

@views.route('/calendar')
def calendar():
    return render_template("calendar.html", user=current_user)

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
