import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # General Flask Config
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    DEBUG = False
    TESTING = False

    # Database Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(basedir, 'forensic_tool.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # File Upload Config
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'txt', 'csv', 'xlsx', 'xml', 'json'}

    # Security Config
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True

    # Other Configs
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB max file upload size


class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    # This line ensures you're always working with your development database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or f"sqlite:///{os.path.join(basedir, 'dev_forensic_tool.db')}"


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for testing


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///forensic_tool.db'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}