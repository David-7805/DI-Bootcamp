import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'xo4MK99!ds'
DATABASE = 'RestaurantMenuManager'
PORT = '5432'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"INSERT INTO Menu_Items (item_name, item_price) VALUES ('{self.name}', {self.price});"
        cursor.execute(query)
        connection.commit()

    def delete(self):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        query = f"DELETE FROM Menu_Items WHERE item_name = '{self.name}' AND item_price = {self.price};"
        cursor.execute(query)
        connection.commit()

#    def update_2(self, new_name, new_price):
#        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
#        cursor = connection.cursor()
#        query = f"UPDATE Menu_Items SET item_name = '{new_name}', item_price = {new_price} WHERE item_name = '{self.name}' AND item_price = {self.price};"
#        cursor.execute(query)
#        connection.commit()

    def update(self, *args): # I thought it should have been possible to give only one change too
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
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


if __name__ == "__main__":
    item = MenuItem('Pizza', 15)
    item.update_2(25, 'Pita falafel')
# connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
# cursor = connection.cursor()
# query = "SELECT * FROM Menu_Items;"
# cursor.execute(query)
# results = cursor.fetchall()
# connection.close()
# for item in results:
        # print(item)