from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from models.base import Base
from models import product
from database.dbconfig import SQLALCHEMY_DATABASE_URL

# Create engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    echo=False
)

# Create session
async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Session dependency
async def get_session():
    async with async_session() as session:
        yield session

# Create database tables
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)