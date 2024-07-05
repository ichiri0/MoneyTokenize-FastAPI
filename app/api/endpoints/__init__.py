"""
Endpoints API Module
"""

from fastapi import APIRouter

from . import money_tokenize

router = APIRouter()
router.include_router(money_tokenize.router)

__all__ = ['router']
