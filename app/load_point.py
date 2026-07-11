import psycopg2
dbname = "schooldb"
user = "postgres"
password = "postgis"
host = "127.0.0.1"
port = "5433"
conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# 创建新表
create_table_query = '''
CREATE TABLE IF NOT EXISTS points (
index INTEGER
       GENERATED ALWAYS AS IDENTITY
       PRIMARY KEY,
lat FLOAT,
lon FLOAT
)
'''
cursor.execute(create_table_query)
conn.commit()

def store_point(lat,lon):
    insert_point = '''
INSERT INTO points (
        lat,
        lon
    )
    VALUES (%s, %s)
'''
    cursor.execute(insert_point,(lat,lon))
    conn.commit()

print("Table created successfully.")