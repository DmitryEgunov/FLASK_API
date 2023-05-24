import pydantic
from typing import Optional


class CreateAds(pydantic.BaseModel):
    title: str
    description: str
    owner: str


class PatchAds(pydantic.BaseModel):
    title: Optional[str]
    description: Optional[str]
    owner: Optional[str]


