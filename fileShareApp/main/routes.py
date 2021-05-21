from flask import Blueprint
from flask import render_template, url_for, redirect, flash, request, abort, session,\
    Response, current_app, send_from_directory
from fileShareApp import db, bcrypt, mail
from fileShareApp.models import Post, User, Investigations, Kmtracking
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
from fileShareApp.main.utils import investigations_query_util, queryToDict, search_criteria_dictionary_util
# from fileShareApp.dmr.utils
import openpyxl
from werkzeug.utils import secure_filename
import json
import glob

from fileShareApp.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, \
    RequestResetForm, ResetPasswordForm

main = Blueprint('main', __name__)

@main.route("/home")
@login_required
def home():
    return render_template('home.html')

@main.route("/search", methods=["GET","POST"])
@login_required
def search():
    print('*TOP OF def search()*')

    formDict = request.form.to_dict()

    column_names=['id','NHTSA_ACTION_NUMBER', 'MAKE','MODEL','YEAR','COMPNAME','MFR_NAME',
        'ODATE','CDATE','CAMPNO','SUBJECT']
        
    #login takes else
    if request.args.get('query_file_name'):
        query_file_name=request.args.get('query_file_name')
        # print('request.args exists::::',request.args.get('query_file_name'))
        # print('***NOT login path***')
        investigations_query, search_criteria_dictionary = investigations_query_util(query_file_name)
        # investigations_query=investigations_query.filter(getattr(Investigations,'YEAR')>2015).all()
        # print('investigations_query results:::', len(investigations_query))
        # print('search_criteria_dictionary results:::',  search_criteria_dictionary)
        no_hits_flag = False
        if len(investigations_query) ==0:
            no_hits_flag = True
    elif request.args.get('no_hits_flag')==True:
        investigations_query, search_criteria_dictionary = ([],{})
    else:
        query_file_name= 'default_query.txt'
        investigations_query, search_criteria_dictionary = investigations_query_util(query_file_name)
        # investigations_query=investigations_query.filter(getattr(Investigations,'YEAR')>2015).all()
        # print('investigations_query results:::', len(investigations_query))
        no_hits_flag = False
        if len(investigations_query) ==0:
            no_hits_flag = True        
        
    #Make investigations to dictionary for bit table bottom of home screen
    investigations_data = queryToDict(investigations_query, column_names)#List of dicts each dict is row
    #make make_list drop down options
    with open(os.path.join(current_app.config['UTILITY_FILES_FOLDER'],'make_list.txt')) as json_file:
        make_list=json.load(json_file)
        json_file.close()

    if request.method == 'POST':
        print('!!!!in POST method no_hits_flag:::', no_hits_flag)
        formDict = request.form.to_dict()
        if formDict.get('refine_search_button'):
            print('@@@@@@ refine_search_button')
            query_file_name = search_criteria_dictionary_util(formDict)
            return redirect(url_for('main.search', query_file_name=query_file_name, no_hits_flag=no_hits_flag))


    return render_template('search.html',table_data = investigations_data, column_names=column_names,
        len=len, make_list = make_list, query_file_name=query_file_name,
        search_criteria_dictionary=search_criteria_dictionary,str=str)

@main.route("/reports", methods=["GET","POST"])
@login_required
def reports():
    return "This is the reports page"








