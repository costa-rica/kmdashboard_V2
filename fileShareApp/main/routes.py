from flask import Blueprint
from flask import render_template, url_for, redirect, flash, request, abort, session,\
    Response, current_app, send_from_directory
from fileShareApp import db, bcrypt, mail
from fileShareApp.models import Post, User, Investigations
# from fileShareApp.main.forms import EmployeeForm, AddRestaurantForm, DatabaseForm, AddRoleForm
from flask_login import login_user, current_user, logout_user, login_required
import secrets
import os
from PIL import Image
from datetime import datetime, date, time
import datetime
from sqlalchemy import func, desc
import pandas as pd
import io
from wsgiref.util import FileWrapper
import xlsxwriter
from flask_mail import Message
# from fileShareApp.main.utils 
# from fileShareApp.dmr.utils
import openpyxl
from werkzeug.utils import secure_filename
import json
import glob

from fileShareApp.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, \
    RequestResetForm, ResetPasswordForm

main = Blueprint('main', __name__)

# @users.route("/register", methods=["GET","POST"])
# def register():
    # if current_user.is_authenticated:
        # return redirect(url_for('users.home'))
    # form= RegistrationForm()
    # if form.validate_on_submit():
        # hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        # userPermission1=userPermission(form.email.data)
        # if userPermission1[0]:
            # user=User(username=form.username.data, email=form.email.data, password=hashed_password,
            # permission=userPermission1[1])
        # else:
            # user=User(username=form.username.data, email=form.email.data, password=hashed_password)
        # db.session.add(user)
        # db.session.commit()
        # flash(f'You are now registered! You can login.', 'success')
        # return redirect(url_for('users.login'))
    # return render_template('register.html', title='Register',form=form)



# @main.route("/")
# @main.route("/login", methods=["GET","POST"])
# def login():
    # if current_user.is_authenticated:
        # return redirect(url_for('buckets.main_bucket'))
    # form = LoginForm()
    # if form.validate_on_submit():
        # user=User.query.filter_by(email=form.email.data).first()
        # if user and bcrypt.check_password_hash(user.password,form.password.data):
            # login_user(user, remember=form.remember.data)
            # next_page = request.args.get('next')
            need to use args.get instead of square brackets adn key name because tthat would throw error if key
            doesnt' exist. Using args.get returns None if there is no key
            ^^^^^***This is very useful*** ^^^^^^
            # return redirect(next_page) if next_page else redirect(url_for('buckets.main_bucket'))
            ^^^ another good thing turnary condition ^^^
        # else:
            # flash('Login unsuccessful', 'danger')
    # return render_template('index.html', form = form)
    return 'Hello Buckets!'    




