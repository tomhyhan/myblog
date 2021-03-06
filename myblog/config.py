import os




class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('USER_NAME')
    MAIL_PASSWORD = os.environ.get('USER_PASSWORD')
    MAIL_DEFAULT_SENDER = 'noreply@gmail.com'
    SECURITY_EMAIL_SENDER = 'noreply@gmail.com'


