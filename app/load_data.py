import psycopg2
import json
from app.conectsetting import global_port
dbname = "schooldb"
user = "postgres"
password = "postgis"
host = "127.0.0.1"
port = global_port


# 获取结果

def load_pointdata() ->list[dict]:

    conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query = "SELECT index,ST_AsGeoJSON(point) FROM points;"
    cursor.execute(query)

    results = cursor.fetchall()
    points = []
    for row in results:
        point = {
            "index":row[0],
            "geometry":json.loads(row[1])
        }
        points.append(point)
    return points


def load_line()->list:
    conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query = "SELECT index,ST_AsGeoJSON(line) FROM lines;"
    cursor.execute(query)

    results = cursor.fetchall()
    lines = []
    for row in results:
        line = {
            "index":row[0],
            "geometry":json.loads(row[1])
        }
        lines.append(line)
    return lines

def load_polygon()->list:
    conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query = "SELECT index,ST_AsGeoJSON(poly) FROM polygons;"
    cursor.execute(query)

    results = cursor.fetchall()
    polys = []
    for row in results:
        poly = {
            "index":row[0],
            "geometry":json.loads(row[1])
        }
        polys.append(poly)
    return polys
    


    


