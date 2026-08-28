from uuid import uuid4

import httpx
from fastapi import HTTPException

from app.core.config import get_settings
from app.models.posts import PublishRequest, PublishResponse, StatusResponse


class MetaClient:
    def __init__(self) -> None:
        self.settings = get_settings()

    async def publish(self, channel: str, payload: PublishRequest) -> PublishResponse:
        if self.settings.meta_mode == "mock":
            return PublishResponse(
                ok=True,
                channel=channel,
                external_id=f"mock_{channel}_{uuid4().hex[:12]}",
                status="mocked",
                campaign_id=payload.campaign_id,
                request_id=payload.request_id,
                mode="mock",
            )

        return await self._publish_live(channel, payload)

    async def _publish_live(self, channel: str, payload: PublishRequest) -> PublishResponse:
        token = self.settings.meta_access_token
        if not token:
            raise HTTPException(status_code=503, detail="META_ACCESS_TOKEN is not configured")

        # La implementación live se completa por canal después de validar las
        # credenciales y permisos disponibles en la app Meta de la POC.
        raise HTTPException(
            status_code=501,
            detail=f"Live publishing for {channel} is not enabled yet; use META_MODE=mock",
        )

    async def status(self, external_id: str) -> StatusResponse:
        if self.settings.meta_mode == "mock":
            return StatusResponse(ok=True, external_id=external_id, status="mocked", mode="mock")

        raise HTTPException(status_code=501, detail="Live status lookup is not enabled yet")


meta_client = MetaClient()
