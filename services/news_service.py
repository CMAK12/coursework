from repositories.news_repository import NewsRepository
from schemas.news_schema import NewsUpdate, NewsCreate
from uuid import UUID

class NewsService:
    def __init__(self):
        self.repository = NewsRepository()

    async def list_news(self):
        return await self.repository.get_list_news()

    async def get_news(self, news_id: UUID):
        return await self.repository.get_news(news_id)

    async def add_news(self, news: NewsCreate):
        return await self.repository.create_news(news)

    async def update_news(self, news_id: UUID, news_data: NewsUpdate):
        return await self.repository.update_news(news_id, news_data)

    async def delete_news(self, news_id: UUID):
        return await self.repository.delete_news(news_id)
