from fastapi import APIRouter

from app.core.config import get_settings

router = APIRouter(tags=["health"])


@router.get("/health")
def health() -> dict:
    settings = get_settings()
    return {
        "ok": True,
        "service": settings.app_name,
        "environment": settings.app_env,
        "meta_mode": settings.meta_mode,
        "channels": ["facebook", "instagram", "threads"],
    }
