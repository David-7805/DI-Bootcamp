import psycopg2

db_params = {
    "host": 'localhost',
    "user": 'postgres',
    "password": 'xo4MK99!ds',
    "port": '5432',
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()
connection.autocommit = True

cursor.execute("""DROP DATABASE if exists countries;""")
cursor.execute("""CREATE DATABASE countries;""")
if connection:
    cursor.close()
    connection.close()