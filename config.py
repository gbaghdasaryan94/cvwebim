from os import environ, path

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

    # Configuring MySQL (JawsDB Maria) connection
    MYSQL_HOST = 'f80b6byii2vwv8cx.chr7pe7iynqr.eu-west-1.rds.amazonaws.com'
    MYSQL_USER = 'vqc83wwwb68h5ox9'
    MYSQL_PASSWORD = 'jv48oyhkkncd66fl'
    MYSQL_DB = 'ihn0vezkznn35z74'
    
    # Initialize MySQL
    # Set up Flask-Session to store sessions in JawsDB Maria
    SESSION_TYPE = 'sqlalchemy'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
   

    # SQLAlchemy Database URI for JawsDB Maria (using pymysql)
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'

    # Database
    SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQLALCHEMY_TRACK_MODIFICATIONS")
    # FLASK_APP="wsgi.py"
    # FLASK_DEBUG=1
    APP_CONFIG_FILE="config.ini"

    SQLALCHEMY_TRACK_MODIFICATIONS=False

    MAIL_SERVER = 'smtp.beget.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    # MAIL_DEBUG = True 
    MAIL_USERNAME = 'garnik_cv@yopmail.com'
    # MAIL_PASSWORD = 'Instigate555'
    MAIL_DEFAULT_SENDER = ("IMsurvey Contact Form",'imsurvey@kit.am')
    MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = False1
    MAIL_ASCII_ATTACHMENTS = False
