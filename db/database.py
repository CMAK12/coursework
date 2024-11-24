from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL

class Database:
    _instance = None
    _engine = create_async_engine(DATABASE_URL, echo=True, future=True)
    _session = sessionmaker(bind=_engine, expire_on_commit=False, class_=AsyncSession)

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_session(self) -> AsyncSession:
        return self._session()

database = Database()
