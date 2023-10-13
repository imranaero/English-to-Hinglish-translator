from fastapi import APIRouter
from api.services.translate.translator import translator

router = APIRouter()


@router.post("/translator")
async def translation(text: str):
    output = await translator(text)
    return output
