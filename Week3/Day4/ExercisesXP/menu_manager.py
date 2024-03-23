import psycopg2


class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        query = f"SELECT * FROM Menu_Items WHERE item_name = '{name}';"
        cursor.execute(query)
        result = cursor.fetchall()
        if result == []:
            return None
        else:
            return result

    @classmethod
    def get_by_name_and_price(cls, name, price):
        query = f"SELECT * FROM Menu_Items WHERE item_name = '{name}' AND item_price = {price};"
        cursor.execute(query)
        result = cursor.fetchall()
        if result == []:
            return None
        else:
            return result

    @classmethod
    def all_items(cls):
        query = f"SELECT * FROM Menu_Items;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result


db_params = {
    "host": 'localhost',
    "user": 'postgres',
    "password": 'xo4MK99!ds',
    "port": '5432',
    "dbname": 'RestaurantMenuManager'
}
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()
    # print(MenuManager.get_by_name('Beef Stew'))
    # print(MenuManager.get_by_name('Sandwich'))
    # print(MenuManager.all_items())
    # print(MenuManager.get_by_name_and_price('Pita falafel', 25))
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")
# finally:
    # if connection:
        # cursor.close()
        # connection.close()

