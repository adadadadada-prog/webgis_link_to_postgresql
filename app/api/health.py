from fastapi import APIRouter
from sqlalchemy import text

from app.core.database import engine


router = APIRouter(prefix="/health", tags=["health"])

print("xxxxxxxxx")
@router.get("/db")
async def check_database():
    async with engine.connect() as conn:
        postgres_result = await conn.execute(text("SELECT version();"))
        postgis_result = await conn.execute(text("SELECT PostGIS_Version();"))

        postgres_version = postgres_result.scalar()
        postgis_version = postgis_result.scalar()

    return {
        "ok": True,
        "postgres": postgres_version,
        "postgis": postgis_version,
    }