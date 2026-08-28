from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.posts import router as posts_router

app = FastAPI(
    title="Forestin - Meta API",
    description="API central para publicaciones Meta consumida por Forestin - Informa.",
    version="0.1.0",
)

app.include_router(health_router)
app.include_router(posts_router)


@app.get("/", tags=["root"])
def root() -> dict:
    return {
        "service": "Forestin - Meta",
        "version": "0.1.0",
        "docs": "/docs",
        "health": "/health",
    }
