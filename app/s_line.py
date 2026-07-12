import psycopg2
from app.conectsetting import global_port

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
CREATE TABLE IF NOT EXISTS lines (
index INTEGER
       GENERATED ALWAYS AS IDENTITY
       PRIMARY KEY,
line geometry(LineString, 4326)
)
'''
cursor.execute(create_table_query)
conn.commit()

def store_line(linelist:dict):
    line = []
    linesinglist = linelist.get("pointlist")
    for point in linesinglist:
        lat = point.get("lat")
        lon = point.get("lng")
        line.append(f"{lon} {lat}")
    
    print(line)
    line_wkt = (
        "LINESTRING("
        + ", ".join(line)
        + ")"
    )
    insert_line = """
    INSERT INTO lines (line)
    VALUES (
        ST_GeomFromText(
            %s,
            4326
        )
    )
    """
    cursor.execute(insert_line,(line_wkt,))
    conn.commit()

