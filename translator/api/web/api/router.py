from fastapi.routing import APIRouter

from api.web.api import docs, english_hinglish

api_router = APIRouter()
api_router.include_router(docs.router)
api_router.include_router(english_hinglish.router)
