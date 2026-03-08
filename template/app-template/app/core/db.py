{% if database == "postgres" %}
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from app.core.config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

{% else %}
import motor.motor_asyncio
from beanie import init_beanie
from app.core.config import settings

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)
    # Define models here and pass them to init_beanie
    await init_beanie(database=client.get_default_database(), document_models=[])

async def get_db():
    # MongoDB access typically doesn't need a generator for sessions in Beanie
    pass
{% endif %}
