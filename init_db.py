import asyncio
from app.core.database import Base,engine
from app.models import spatial

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("database tables created")

if __name__  == "__main__":
    asyncio.run(main())