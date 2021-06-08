# from fileShareApp import db
# from fileShareApp.models import Post, User, Investigations, Kmtracking,Km_saved_queries
# import os
# from flask import current_app
# import json
# from datetime import date, datetime
# from flask_login import current_user
# import logging
# import openpyxl
# import xlsxwriter
# import pandas as pd



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
from fileShareApp.main.utils import investigations_query_util, queryToDict, search_criteria_dictionary_util,\
    updateInvestigation, create_categories_xlsx
# from fileShareApp.dmr.utils
# from fileShareApp.main.utils2 import create_categories_xlsx2
import openpyxl
from werkzeug.utils import secure_filename
import json
import glob
import shutil
# import logging


def create_categories_xlsx2(excel_file_name):
    print('in build_excel_report  utility')
    # excelObj_test=pd.ExcelWriter('test_build_excelWriter.xlsx')
    # print('in build_excel_report_test')
    # excelObj_test.close()
    # excelObj=pd.ExcelWriter(os.path.join(current_app.config['UTILITY_FILES_FOLDER'],excel_file_name))
    print('in build_excel_report  utility')
    # columnNames=Investigations.__table__.columns.keys()
    # colNamesDf=pd.DataFrame([columnNames],columns=columnNames)
    # colNamesDf.to_excel(excelObj,sheet_name='Investigation Data', header=False, index=False)
    print('added column names')

    queryDf = pd.read_sql_table('investigations', db.engine)
    queryDf.to_excel(excelObj,sheet_name='Investigation Data', header=False, index=False,startrow=1)
    print('added database data')
    inv_data_workbook=excelObj.book
    notes_worksheet = inv_data_workbook.add_worksheet('Notes')
    notes_worksheet.write('A1','Created:')
    print('wrote some stuff')
    notes_worksheet.set_column(1,1,len(str(datetime.datetime.now())))
    time_stamp_format = inv_data_workbook.add_format({'num_format': 'mmm d yyyy hh:mm:ss AM/PM'})
    notes_worksheet.write('B1',datetime.datetime.now(), time_stamp_format)
    excelObj.close()
    return print('end')
    # current_app.logger.info('succesfully created')