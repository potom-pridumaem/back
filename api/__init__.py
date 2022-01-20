from fastapi import APIRouter

from .discord import router as discord_router
from .web import router as web_router

router = APIRouter(prefix="/api")
router.include_router(discord_router)
router.include_router(web_router)
