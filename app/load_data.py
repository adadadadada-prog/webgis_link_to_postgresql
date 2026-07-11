import psycopg2
dbname = "schooldb"
user = "postgres"
password = "postgis"
host = "127.0.0.1"
port = "5433"


# 获取结果

def load_alldata() ->list[dict]:

    conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()

    query = "SELECT * FROM points;"
    cursor.execute(query)

    results = cursor.fetchall()
    points = []


    for row in results:
       point = {"index":row[0],
                "lat":row[1],
                "lon":row[2]}
       points.append(point)
        
    return points




