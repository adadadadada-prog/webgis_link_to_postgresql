import psycopg2
dbname = "schooldb"
user = "postgres"
password = "postgis"
host = "127.0.0.1"
port = "5433"
conn_string = f"host={host} port={port} dbname={dbname} user={user} password={password}"
conn = psycopg2.connect(conn_string)
cursor = conn.cursor()

# 如果表已存在，则删除


# 创建新表
create_table_query = '''
CREATE TABLE EMPLOYEE (
FIRST_NAME CHAR(20) NOT NULL,
LAST_NAME CHAR(20),
AGE INT,
SEX CHAR(1),
INCOME FLOAT
)
'''
cursor.execute(create_table_query)
conn.commit()
print("Table created successfully.")