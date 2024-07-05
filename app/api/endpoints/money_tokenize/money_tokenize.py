from fastapi import APIRouter, status
import os

from fastapi.exceptions import HTTPException

from app.core.tokenize_processing.tokenize_processing import convert_amount_to_words

router = APIRouter()

@router.get("/")
async def get(number: int | float = "1212410.77") -> dict:

    try:
        

        # Ввод суммы с клавиатуры
        amount = float(number)
        words = convert_amount_to_words(amount)
        print(words)


        return {
            "data": words
        }

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=ex
        )
    