import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'xo4MK99!ds'
DATABASE = 'RestaurantMenuManager'
PORT = '5432'

class MenuManager:

    @classmethod
    def get_by_name(cls, name):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"SELECT * FROM Menu_Items WHERE item_name = '{name}';"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        if result == []:
            return None
        else:
            return result

    @classmethod
    def get_by_name_and_price(cls, name, price):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"SELECT * FROM Menu_Items WHERE item_name = '{name}' AND item_price = {price};"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        if result == []:
            return None
        else:
            return result

    @classmethod
    def all_items(cls):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"SELECT * FROM Menu_Items;"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result

if __name__ == "__main__":
    print(MenuManager.get_by_name('Beef Stew'))
    print(MenuManager.get_by_name('Sandwich'))
    print(MenuManager.all_items())

