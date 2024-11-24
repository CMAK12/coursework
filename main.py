from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.exc import NoResultFound
from uuid import UUID

from services.news_service import NewsService
from schemas.news_schema import NewsRead, NewsUpdate, NewsCreate

app = FastAPI(title="News API")
news_service = NewsService()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://127.0.0.1:5500', 'http://localhost:5500'], # Port 5500 is Live Server's default port in VSC
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Take list of news
@app.get("/api/news/")
async def read_news():
    return await news_service.list_news()

# Take single news
@app.get("/api/news/{news_id}", response_model=NewsRead)
async def read_news(news_id: UUID):
    try:
        return await news_service.get_news(news_id)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="News not found")

# Create news
@app.post("/api/news/", response_model=NewsRead)
async def create_news(news_data: NewsCreate):
    return await news_service.add_news(news_data)

# Update news
@app.put("/api/news/{news_id}", response_model=NewsUpdate)
async def update_news(news_id: UUID, news: NewsUpdate):
    try:
        return await news_service.update_news(news_id, news)
    except NoResultFound:
        raise HTTPException(status_code=404, detail="News not found")

# Delete news
@app.delete("/api/news/{news_id}", response_model=dict)
async def delete_news(news_id: UUID):
    try:
        await news_service.delete_news(news_id)
        return {"detail": "News deleted"}
    except NoResultFound:
        raise HTTPException(status_code=404, detail="News not found")