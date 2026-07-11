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
CREATE TABLE IF NOT EXISTS polygons (
index INTEGER
       GENERATED ALWAYS AS IDENTITY
       PRIMARY KEY,
poly GEOMETRY(Polygon, 4326)
)
'''
cursor.execute(create_table_query)
conn.commit()

def store_polygon(points:dict):
    all_point = []
    pointlist = points.get("pointlist")
    for point in pointlist:
        lat = point.get("lat")
        lon = point.get("lng")
        all_point.append(f"{lon} {lat}")

    last = all_point[0]
    all_point.append(last)
    poly_wkt = (
        "POLYGON(("
        + ", ".join(all_point)
        + "))"
    )
   
    insert_polygon = """
    INSERT INTO polygons (poly)
    VALUES (
        ST_GeomFromText(
            %s,
            4326
        )
    )
    """
    cursor.execute(insert_polygon,(poly_wkt,))
    conn.commit()

