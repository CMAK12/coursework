from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class Source(BaseModel):
    name: str
    url: Optional[str] = None

class NewsBase(BaseModel):
    title: str
    description: str
    content: str
    publishedAt: str
    source: Source
    url: Optional[str] = None
    image: Optional[str] = None

class NewsCreate(NewsBase):
    pass

class NewsUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    content: Optional[str] = None
    url: Optional[str] = None
    image: Optional[str] = None
    publishedAt: Optional[str] = None
    source: Optional[Source] = None

class NewsRead(NewsBase):
    id: UUID


    class Config:
        from_attributes = True
        arbitrary_types_allowed = True