from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from extentions import db
from .models import User
from .forms import RegistrationForm, LoginForm


main = Blueprint('main',__name__)


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print("Form is validated!")
        #check if user already exists
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            flash('Email already exists. Please Log in.', 'warning')
            return redirect(url_for('main.login'))
        
        #Create new user
        new_user = User(
            username = form.username.data,
            email= form.email.data
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Registration Successful! You can now login', 'success')
        return redirect(url_for('main.login')) 
    
    return render_template('register.html', form=form)
    

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful', 'success')
            
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password', 'danger')

    return render_template('login.html', form=form)


@main.route('/logout', methods=['POST'])
def logout():
    logout_user()
    flash('You Have Been Logged Out.', 'succes')
    return redirect(url_for('main.login'))


@main.route('/donate', methods=['POST', 'GET'])
def donate():
    return render_template('donate.html')


@main.route('/campaign', methods=['POST', 'GET'])
def campaign():
    return render_template('campaign.html')


@main.route('/')
def index():
    return render_template('welcome.html')