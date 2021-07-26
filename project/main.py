# main.py flask

from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, role=current_user.role)

@main.route('/profile1')
@login_required
def profile1():
    return render_template('as.html', name=current_user.name, role=current_user.role)

@main.route('/profile2')
@login_required
def profile2():
    return render_template('admin.html', name=current_user.name, role=current_user.role)

@main.route('/profile3')
@login_required
def profile3():
    return render_template('User.html', name=current_user.name, role=current_user.role)
