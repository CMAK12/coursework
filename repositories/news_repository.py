from sqlalchemy import delete, update
from sqlalchemy.exc import NoResultFound
from uuid import UUID
from httpx import AsyncClient, HTTPError

from db.database import database
from models.news import News
from config import GNEWS_API_URL, NEWSAPI_API_URL, NYT_API_URL
from schemas.news_schema import NewsUpdate, NewsCreate
from sqlalchemy.future import select

class NewsRepository:
    async def get_list_news(self):
        # Requesting data to foreign APIs
        try:
            async with AsyncClient() as client:
                # GNews API
                response_gnews = await client.get(GNEWS_API_URL)
                response_gnews.raise_for_status()
                external_gnews = response_gnews.json().get("articles", [])

                # News API
                response_newsapi = await client.get(NEWSAPI_API_URL)
                response_newsapi.raise_for_status()
                external_newsapi = response_newsapi.json().get("articles", [])

                # The New York Times API
                response_nyt = await client.get(NYT_API_URL)
                response_nyt.raise_for_status()
                external_nyt = response_nyt.json().get("results", [])
        except HTTPError as e:
            raise Exception(f"An error occurred: {e}")

        # Getting data from the database
        async with database.get_session() as session:
            result = await session.execute(select(News))
            local_news = result.scalars().all()

        return local_news + external_gnews + external_newsapi + external_nyt # Merging all news APIs

    async def get_news(self, news_id: UUID):
        async with database.get_session() as session:
            result = await session.execute(select(News).where(News.id == news_id))
            news = result.scalar_one_or_none()
            if not news:
                raise NoResultFound("News not found")
            return news

    async def create_news(self, news_data: NewsCreate):
        news = News(**news_data.dict())
        async with database.get_session() as session:
            session.add(news)
            await session.commit()
            return news

    async def update_news(self, news: UUID, news_data: NewsUpdate):
        async with database.get_session() as session:
            await session.execute(
                update(News)
                .where(News.id == news)
                .values(**{k: v for k, v in news_data.dict(exclude_unset=True).items()})
            )
            await session.commit()
            return news_data

    async def delete_news(self, news_id: UUID):
        async with database.get_session() as session:
            await session.execute(delete(News).where(News.id == news_id))
            await session.commit()
            return True