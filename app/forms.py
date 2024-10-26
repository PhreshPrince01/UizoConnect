from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, FloatField, FileField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class CampaignForm(FlaskForm):
    campaign_name = StringField('Campaign Name', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    total_funds = FloatField('Total Funds', validators=[DataRequired()])
    ID_document = FileField('ID Document')
    quotation = StringField('Campaign Quotation')
    submit = SubmitField('Create Campaign')
