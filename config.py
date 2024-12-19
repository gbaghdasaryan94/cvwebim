from os import environ, path
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

class Config:
    """Set Flask configuration vars from .env file."""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    ALLOWED_HOSTS = ['.herokuapp.com']
    APP_ROOT = path.dirname(path.abspath(__file__))
    
    APP_STATIC_ROOT = path.abspath('IMSurvey')
    IMAGE_UPLOADS = 'static/uploads'

    # ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
    
    # UPLOAD_FOLDER = path.join(APP_ROOT, 'IMSurvey/static/uploads')

    # Ensure templates are auto-reloaded
    TEMPLATES_AUTO_RELOAD = True

    # Configure session to use filesystem (instead of signed cookies)


    # Database
    # SQLALCHEMY_DATABASE_URI = "sqlite:///survey.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    # FLASK_APP="wsgi.py"
    # FLASK_DEBUG=1
    APP_CONFIG_FILE="config.ini"

    # Configuring Postgres (JawsDB Maria) connection
    DB_HOST ='c5p86clmevrg5s.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com'
    DB_USERNAME='u3rtin6ohqv1mv'
    DB_PASSWORD ='p9393a802f81f789d0d4f255aa4250d1f4cad4959ee166c96852d5f4abd3b6f3d'
    DB_NAME = 'd88sllttan6ntu'

    # SQLALCHEMY_DATABASE_URI="sqlite:///survey.db"
    SQLALCHEMY_DATABASE_URI = f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Set up Flask-Session to store sessions in JawsDB Maria

    # SESSION_TYPE = "sqlalchemy"
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True

    

    

    MAIL_SERVER = 'smtp.beget.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_DEBUG = True 
    MAIL_USERNAME = 'garnik_cv@yopmail.com'
    # MAIL_PASSWORD = 'Instigate555'
    MAIL_DEFAULT_SENDER = ("IMsurvey Contact Form",'imsurvey@kit.am')
    MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False
