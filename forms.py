from wtforms import Form, validators
from wtforms.validators import DataRequired, Length, Optional

from flask_wtf import FlaskForm, RecaptchaField
from wtforms import *

from wtforms import (DataRequired,
                                Email,
                                EqualTo,
                                Length,)


class Donation(Form):
    name = StringField('Name', [
        DataRequired()])
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()])

    contact = StringField('Phone_no',
       [validators.required(), validators.length(min=11, max=10)])
    
    beneficiary = SelectField('Title', [DataRequired()],
                        choices=[('Public', 'public'),
                                 ('Health Sector', 'health sector')])
    
    
    amount_naira= SelectField('Title', [Optional()],
                        choices=[(500, 500),
                                 (1,000, 1000),
                                 (5,000, 5000),
                                 (10,000, 10000),
                                 (50,000, 50000),
                                 (100,000,  100000)])
    

    other_currencies = RadioField('lable', [Optional()],
                        choices=[('dollar', 'Dollar'),
                                 ('pounds', 'Pounds'),
                                 ('euro', 'Euro')])


    amount_other_currencies = SelectField('Title', [DataRequired()],
                        choices=[(50, 50),
                                 (100, 100),
                                 (500, 500),
                                 (1,000, 1000),
                                 (5,000, 5000),
                                 (10,000, 10000)])

    payment_method = RadioField('lable', [DataRequired()],
                        choices=[('bank_transfer', 'Bank Transfer'),
                                 ('remita',  'Remita')
                                 ('voucher', 'Voucher')])
       
    
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')


class Subscribe(FlaskForm):
    """Subscribe."""
    name = StringField('Username', [validators.Length(min=2, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])








