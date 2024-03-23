import psycopg2

db_params = {
    "host": 'localhost',
    "user": 'postgres',
    "password": 'xo4MK99!ds',
    "port": '5432',
    "database": 'countries'
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()
cursor.execute("""DROP TABLE if exists countries;""")
cursor.execute("""
    CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    capital VARCHAR(100),
    flag VARCHAR(10),
    subregion VARCHAR(100),
    population INTEGER
    );
""")
connection.commit()
if connection:
    cursor.close()
    connection.close()