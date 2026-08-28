from fastapi import APIRouter, Depends

from app.core.security import require_api_key
from app.models.posts import PublishRequest, PublishResponse, StatusResponse
from app.services.meta_client import meta_client

router = APIRouter(dependencies=[Depends(require_api_key)])


@router.post("/facebook/posts", response_model=PublishResponse, tags=["facebook"])
async def publish_facebook(payload: PublishRequest) -> PublishResponse:
    return await meta_client.publish("facebook", payload)


@router.post("/instagram/posts", response_model=PublishResponse, tags=["instagram"])
async def publish_instagram(payload: PublishRequest) -> PublishResponse:
    return await meta_client.publish("instagram", payload)


@router.post("/threads/posts", response_model=PublishResponse, tags=["threads"])
async def publish_threads(payload: PublishRequest) -> PublishResponse:
    return await meta_client.publish("threads", payload)


@router.get("/status/{external_id}", response_model=StatusResponse, tags=["status"])
async def get_status(external_id: str) -> StatusResponse:
    return await meta_client.status(external_id)
