import pytest
from uuid import uuid4
from unittest.mock import AsyncMock

from db.database import Database
from schemas.news_schema import NewsCreate, NewsUpdate
from services.news_service import NewsService

@pytest.mark.asyncio
async def test_list_news():
    service = NewsService()
    service.repository.get_list_news = AsyncMock(return_value=[])
    result = await service.list_news()
    assert result == []
    service.repository.get_list_news.assert_called_once()

@pytest.mark.asyncio
async def test_add_news():
    service = NewsService()
    news_data = NewsCreate(
        title="Test Title",
        description="Test Description",
        content="Test Content",
        publishedAt="2024-11-26",
        source={"name": "Test Source"},
    )
    mock_news = news_data.dict()
    mock_news["id"] = uuid4()

    service.repository.create_news = AsyncMock(return_value=mock_news)
    result = await service.add_news(news_data)
    assert result == mock_news
    service.repository.create_news.assert_called_once_with(news_data)

@pytest.mark.asyncio
async def test_is_database_signleton():
    db = Database()
    db1 = Database()
    assert db.__hash__() == db1.__hash__()

@pytest.mark.asyncio
async def test_get_news():
    service = NewsService()
    news_id = uuid4()
    mock_news = {"id": news_id, "title": "Test Title"}

    service.repository.get_news = AsyncMock(return_value=mock_news)
    result = await service.get_news(news_id)
    assert result == mock_news
    service.repository.get_news.assert_called_once_with(news_id)

@pytest.mark.asyncio
async def test_update_news():
    service = NewsService()
    news_id = uuid4()
    update_data = NewsUpdate(title="Updated Title")
    service.repository.update_news = AsyncMock(return_value=update_data)
    result = await service.update_news(news_id, update_data)
    assert result == update_data
    service.repository.update_news.assert_called_once_with(news_id, update_data)
