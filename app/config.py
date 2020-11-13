# config variables that eventually should be retrieved from a .env file
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")

    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_COOKIE_PATH = "/"
    JWT_REFRESH_COOKIE_PATH = "/token/refresh"
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")

    UPLOAD_FOLDER = "uploads"
    MAX_CONTENT_LENGTH = 1 * 1024 * 1024
    ML_FOLDER = "ml"

    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://root:{os.getenv('SQL_ROOT_PASSWORD')}@db:3306/hackathon_portal"
