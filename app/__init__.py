"""
Init App Module
"""

from fastapi import FastAPI

from app import api
from app.core import settings

app = FastAPI(
    title=settings.APP_TITLE,
    root_path=settings.APP_PATH,
    version=settings.APP_VERSION,
    description=settings.app_description,

)

app.include_router(api.api_router)
