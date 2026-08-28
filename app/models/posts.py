from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class PublishRequest(BaseModel):
    app_name: str = Field(min_length=1, max_length=100)
    campaign_id: str | None = Field(default=None, max_length=100)
    request_id: str | None = Field(default=None, max_length=100)
    message: str = Field(min_length=1, max_length=10000)
    image_url: HttpUrl | None = None


class PublishResponse(BaseModel):
    ok: bool
    provider: Literal["meta"] = "meta"
    channel: Literal["facebook", "instagram", "threads"]
    external_id: str
    status: Literal["mocked", "published", "failed"]
    campaign_id: str | None = None
    request_id: str | None = None
    mode: Literal["mock", "live"]


class StatusResponse(BaseModel):
    ok: bool
    external_id: str
    status: str
    mode: Literal["mock", "live"]
