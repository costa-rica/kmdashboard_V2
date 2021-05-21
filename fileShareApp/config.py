import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY_DMR')
    SQLALCHEMY_DATABASE_URI = r'sqlite:///D:\databases\fileShareApp\fileShareApp.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD_CBC')
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME_CBC')
    DEBUG = True
    UPLOADED_FILES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/files')
    UTILITY_FILES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/utility_files')
    QUERIES_FOLDER = os.path.join(os.path.dirname(__file__), 'static/queries')