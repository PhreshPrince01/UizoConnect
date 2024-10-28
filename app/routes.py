from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from extentions import db
from .models import Campaign, User
from .forms import CampaignForm, RegistrationForm, LoginForm


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
    campaigns = Campaign.query.filter_by(user_id = 5).order_by(Campaign.date_started.desc()).all()

    return render_template('donate.html', campaign = campaigns)


@main.route('/payment-method', methods=['GET'])
def payment_method():
    campaign_id = request.args.get('campaign_id')
    campaign_name = request.args.get('campaign_name')

    return render_template('paymentMethod.html', campaign_id=campaign_id, campaign_name=campaign_name)



@main.route('/campaign', methods=['POST', 'GET'])
def campaign():
    form = CampaignForm()
    if form.validate_on_submit():

        id_doc = Campaign.save_file(form.ID_document.data)

        new_campaign = Campaign(
            campaign_name = form.campaign_name.data,
            description = form.description.data,
            total_funds = form.total_funds.data,
            ID_document = id_doc,
            user_id =5,
            quotation = form.quotation.data
        )
        db.session.add(new_campaign)
        db.session.commit()
        flash("Campaign added susscessfully. Pending confirmation", "success")
        return redirect(url_for('main.index'))
    else:
        print(form.errors)
        
    return render_template('campaign.html', form=form)




@main.route('/')
def index():
    return render_template('welcome.html')