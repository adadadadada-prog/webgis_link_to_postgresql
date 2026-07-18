import psycopg2
from app.conectsetting import global_port
import json
dbname = "schooldb"
user = "postgres"
password = "postgis"
host = "127.0.0.1"
port = global_port
conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# 创建新表
create_table_query = '''
CREATE TABLE IF NOT EXISTS points (
index INTEGER
       GENERATED ALWAYS AS IDENTITY
       PRIMARY KEY,
point geometry(Point, 4326)
)
'''
cursor.execute(create_table_query)
conn.commit()

def store_point(geodata):
    insert_point = '''
INSERT INTO points (point)
values (
    ST_GeomFromGeoJSON(%s)
    )
    RETURNING index;
'''
    geo_str = json.dumps(geodata) 
    cursor.execute(insert_point,(geo_str,))
    new_index = cursor.fetchone()[0]
    conn.commit()
    return {"new_index":new_index}

