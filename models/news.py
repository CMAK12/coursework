from uuid import uuid4

from sqlalchemy import Column, JSON, String, Text, Uuid
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class News(Base):
    __tablename__ = "news"

    id = Column(Uuid, primary_key=True, nullable=False, index=True, default=uuid4())
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    content = Column(Text, nullable=True)
    url = Column(String, nullable=True)
    image = Column(String, nullable=True)
    publishedAt = Column(String, nullable=True)
    source = Column(JSON, nullable=True)
