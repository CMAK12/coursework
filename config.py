from dotenv import load_dotenv

load_dotenv()

# PostgreSQL connection string
DATABASE_URL = "postgresql+asyncpg://postgres:123@localhost:5432/newsdb"

# API keys
_GNEWS_API_KEY = "a0957ee5b78338d4992d5541efdb7e66"
_NEWSAPI_API_KEY = "779e60c18504444b826a7e350149bea4"
_NYT_API_KEY = "JZ2VrkXcqNJYJkwn9tY0lzuS1xarptUx"

# Foreign APIs
GNEWS_API_URL = f"https://gnews.io/api/v4/search?q=example&lang=en&country=us&apikey={_GNEWS_API_KEY}"
NEWSAPI_API_URL = f"https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={_NEWSAPI_API_KEY}"
NYT_API_URL = f"https://api.nytimes.com/svc/topstories/v2/arts.json?api-key={_NYT_API_KEY}"