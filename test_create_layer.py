import asyncio

from sqlalchemy import text

from app.core.database import AsyncSessionLocal
from app.services.layer_manager import create_feature_table


async def main():
    table_name = "test_point_features"
    geometry_type = "Point"
    srid = 4326

    async with AsyncSessionLocal() as db:
        await db.execute(text(f"DROP TABLE IF EXISTS {table_name};"))

        await create_feature_table(
            db=db,
            table_name=table_name,
            geometry_type=geometry_type,
            srid=srid,
        )

        await db.commit()

    print("feature table created:", table_name)


if __name__ == "__main__":
    asyncio.run(main())