import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host: str = os.environ.get('DATABASE_HOST')
    database_port: int = os.environ.get('DATABASE_PORT')
    database_user: str = os.environ.get('DATABASE_USER')
    database_password: str = os.environ.get('DATABASE_PASSWORD')
    database_name: str = os.environ.get('DATABASE_NAME')
