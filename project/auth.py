# auth.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from . import db
from itertools import *
from .scanthread import scan
import sys


auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()
    role = user.role
    

    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    if role == "Administrateur-Supreme" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile1'))
    
    if role == "Administrateur-Classique" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile2'))
    
    if role == "User" : 
        login_user(user, remember=remember)
        return redirect(url_for('main.profile3'))
    


@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    role = request.form.get('role')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = User(email=email, name=name, role=role, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@auth.route('/password-change')
@login_required
def changement():
    return render_template('password-change.html')


@auth.route('/password-change', methods=['POST'])
@login_required
def changement_post():
    old_pwd = request.form.get('old')
    new1 = request.form.get('new1')
    new2 = request.form.get('new2')
    email_pwd = current_user.email
    flash (email_pwd)
    
    if new1 != new2:
        flash('Les mots de passe sont differents')
        return redirect(url_for('auth.changement'))
        
    
    test_pwd = User.query.filter_by(email=email_pwd).first()
    
    if not check_password_hash(test_pwd.password, old_pwd): 
        flash('Mot de passe incorrect')
    
    change_pwd = User.query.filter_by(email=email_pwd).update({User.password: generate_password_hash(new2, method='sha256') })
    

    db.session.commit()
    
    return redirect(url_for('auth.login'))


@auth.route('/management')
@login_required
def management():
    ids = User.query.with_entities(User.id).all()
    nom = User.query.with_entities(User.name).all()
    mail = User.query.with_entities(User.email).all()
    role = User.query.with_entities(User.role).all()
    
    
    return render_template('mngt.html', ids=ids, nom=nom, mail=mail, role=role, zip=zip )


@auth.route('/management', methods=['POST'])
@login_required
def management_post():
    
    email=request.form.get('suppr')
    
    """ User.query.filter_by(email=email).delete() """
    suppr=User.query.filter_by(email=email).first()
    
    db.session.delete(suppr)
    db.session.commit()
    flash(email,'a été supprimé')



    
    return redirect(url_for('auth.management'))


@auth.route('/port')
@login_required
def scan_port():
    
    read_scan=print(list)
    
    """read_scan=print(sys.stdout.read()) 
    read_scan=sys.stdout """
    
    return render_template('port.html', read_scan=read_scan)