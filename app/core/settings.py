"""
Settings
"""

import os
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # env_path = os.path.join(os.path.dirname(__file__), ".env")
    

    # APP
    APP_PATH: str
    APP_TITLE: str
    APP_VERSION: str
    APP_SECRET_KEY: str

    @property
    def app_description(self):
        with open('README.md', 'r', encoding='utf-8') as f:
            return f.read()


    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding='utf-8', case_sensitive=True
    )



settings = Settings()
print(settings)
