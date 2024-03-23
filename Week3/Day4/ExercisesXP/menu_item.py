import psycopg2


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES ('{self.name}', {self.price});"
        cursor.execute(query)
        connection.commit()

    def delete(self):
        query = f"DELETE FROM Menu_Items WHERE item_name = '{self.name}' AND item_price = {self.price};"
        cursor.execute(query)
        connection.commit()

    def update(self, *args): # I thought it should have been possible to give only one change too
        new_name = self.name
        new_price = self.price
        for update in args:
            if type(update) == str:
                new_name = update
            if type(update) == int:
                new_price = update
        query = f"UPDATE Menu_Items SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}' AND item_price = {self.price};"
        cursor.execute(query)
        connection.commit()


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
        # item = MenuItem('Falafel burger', 10)
        # item.delete()
        # query = "SELECT * FROM Menu_Items ORDER BY item_id;"
        # cursor.execute(query)
        # results = cursor.fetchall()
        # for item in results:
        #     print(item)
except (Exception, psycopg2.Error) as error:
    print(f"Error connecting to the database: {error}")
# finally:
    # if connection:
        # cursor.close()
        # connection.close()