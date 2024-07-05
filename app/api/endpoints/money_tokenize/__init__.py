from fastapi import APIRouter

from . import money_tokenize

router = APIRouter(prefix='/money_tokenize', tags=['money_tokenize'])
router.include_router(money_tokenize.router)

__all__ = ['router']
