import requests
from random import choices
import psycopg2

response = requests.get('https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population')
print(response.status_code)
list_of_countries = response.json()
list_random_countries = choices(list_of_countries, k = 10)

db_params = {
    "host": 'localhost',
    "user": 'postgres',
    "password": 'xo4MK99!ds',
    "port": '5432',
    "database": 'countries'
}

connection = psycopg2.connect(**db_params)
cursor = connection.cursor()

for country in list_random_countries:
    query = f"""
    INSERT INTO countries(name, capital, flag, subregion, population)
    VALUES ('{country['name']['common']}', '{country['capital'][0]}', '{country['flag']}', '{country['subregion']}',
    {country['population']});"""
    cursor.execute(query)
    connection.commit()

if connection:
    cursor.close()
    connection.close()
