import psycopg2
import menu_manager
import menu_item

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'xo4MK99!ds'
DATABASE = 'RestaurantMenuManager'
PORT = '5432'

def show_user_menu():
    print('View an Item (V)')
    print('Add an Item (A)')
    print('Delete an Item (D)')
    print('Update an Item (U)')
    print('Show the Menu (S)')
    print('Exit the Program (X)')
    action = input('>>>: ')
    if action.upper() == 'V':
        pass


def add_item_to_menu():
    item_name = input('Please enter the name of the item that you want to add: ')
    item_price = int(input('Please enter the price of the item that you want to add: '))
    new_item = menu_item.MenuItem(item_name, item_price)
    new_item.save()
    if menu_manager.MenuManager.get_by_name(item_name):
        print('Item was added successfully.')


def remove_item_from_menu(): # Needs to be worked on
    item_name = input('Please enter the name of the item you want to delete: ')
    item_price = int(input('Please enter the price of the item you want to delete: '))
    item_to_be_deleted = menu_item.MenuItem(item_name, item_price)
    if not menu_manager.MenuManager.get_by_name(item_name):
        print('You entered an item that is not on the menu.')
    else:
        item_to_be_deleted.delete()
        if not menu_manager.MenuManager.get_by_name(item_name):
            print('Item was deleted successfully.')
        else:
            print('The price you entered for the item was incorrect.')


def update_item_from_menu(): # Needs to be worked on
    item_name = input('Please enter the name of the item you want to update: ')
    item_price = int(input('Please enter the price of the item you want to update: '))
    new_name = input('Please enter a new name for the item: ')
    new_price = int(input('Please enter a new price for the item: '))
    item_to_be_updated = menu_item.MenuItem(item_name, item_price)
    item_to_be_updated.update(new_name, new_price)
    if menu_manager.MenuManager.get_by_name_and_price(new_name, new_price):
        print("Item was updated successfully")
    else:
        print("Unfortunately, there was an error.")

def show_restaurant_menu():
    whole_menu = menu_manager.MenuManager.all_items()
    whole_menu.sort()
    for item in whole_menu:
        print(f'{item[0]}. {item[1]} {item[2]}')


update_item_from_menu()