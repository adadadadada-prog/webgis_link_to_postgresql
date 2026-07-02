from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

ALLOWED_GEOMETRY_TYPES = {"Point", "LineString", "Polygon"}

async def create_feature_table(db:AsyncSession,table_name: str,geometry_type: str,srid: int = 4326,):
    sql = f"""
     CREATE TABLE {table_name} (
        id SERIAL PRIMARY KEY,
        properties JSONB DEFAULT '{{}}'::jsonb,
        geom geometry({geometry_type}, {srid}) NOT NULL,
        created_at TIMESTAMPTZ DEFAULT now(),
        updated_at TIMESTAMPTZ DEFAULT now()
    );
"""
    index_sql = f"""
    CREATE INDEX idx_{table_name}_geom
    ON {table_name}
    USING GIST (geom);
    """
    await db.execute(text(sql))
    await db.execute(text(index_sql))

    