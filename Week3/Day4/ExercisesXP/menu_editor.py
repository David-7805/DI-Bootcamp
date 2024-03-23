import psycopg2
import menu_manager
import menu_item


def show_user_menu():
        print('\nWelcome to the restaurant menu editor!\nPlease choose:')
        print('View an Item (V)')
        print('Add an Item (A)')
        print('Delete an Item (D)')
        print('Update an Item (U)')
        print('Show the Menu (S)')
        print('Exit the Program (X)')
        action = input('>>>: ')
        return action

def try_string_to_number(string):
    try:
        nearest_int = round(float(string))
    except ValueError:
        print('Please enter a number')
        nearest_int = 'str'
    return nearest_int

def view_an_item():
    item_name = input('Please enter the name of the item that you want to view: ')
    item = menu_manager.MenuManager.get_by_name(item_name)
    print(item)


def add_item_to_menu():
    item_name = input('Please enter the name of the item that you want to add: ')
    item_price = 'str'
    while item_price == 'str':
        item_price = input('Please enter the price of the item that you want to add: ')
        item_price = try_string_to_number(item_price)
    new_item = menu_item.MenuItem(item_name, item_price)
    new_item.save()
    if menu_manager.MenuManager.get_by_name(item_name):
        print('\nItem was added successfully.')
    else:
        print('\nUnfortunately, the item was not added to the menu.')


def remove_item_from_menu():
    item_name = input('Please enter the name of the item you want to delete: ')
    item_price = 'str'
    while item_price == 'str':
        item_price = input('Please enter the price of the item you want to delete: ')
        item_price = try_string_to_number(item_price)
    item_to_be_deleted = menu_item.MenuItem(item_name, item_price)
    if not menu_manager.MenuManager.get_by_name_and_price(item_name, item_price):
        print('\nYou entered an item that is not on the menu.')
    else:
        item_to_be_deleted.delete()
        if not menu_manager.MenuManager.get_by_name_and_price(item_name, item_price):
            print('\nItem was deleted successfully.')
        else:
            print('\nSomething went wrong. Item is not deleted.')


def update_item_from_menu():
    original_name = input('Please enter the name of the item you want to update: ')
    original_price = 'str'
    while original_price == 'str':
        original_price = input('Please enter the price of the item you want to update: ')
        original_price = try_string_to_number(original_price)
    item_to_be_updated = menu_item.MenuItem(original_name, original_price)
    new_name = input('Please enter a new name for the item or enter <9999> if you want to keep the name: ')
    new_price = 'str'
    while new_price == 'str':
        new_price = input('Please enter a new price for the item or enter <9999> if you want to keep the price: ')
        new_price = try_string_to_number(new_price)
    if new_name != '9999' and new_price != 9999:
        item_to_be_updated.update(new_name, new_price)
        check_update(new_name, new_price)
    elif new_name != '9999':
        item_to_be_updated.update(new_name)
        check_update(new_name, original_price)
    elif new_price != 9999:
        item_to_be_updated.update(new_price)
        check_update(original_name, new_price)
    else:
        print("\nYou didn't enter any changes")


def check_update(name, price):
    if menu_manager.MenuManager.get_by_name_and_price(name, price):
        print("\nItem was updated successfully")
    else:
        print("\nUnfortunately, there was an error. Please check if you entered the original item correctly!")

def show_restaurant_menu():
    whole_menu = menu_manager.MenuManager.all_items()
    whole_menu.sort()
    for item in whole_menu:
        print(f'{item[0]}. {item[1]} {item[2]}')

def menu_editor():
    in_user_menu = True
    while in_user_menu == True:
        action = show_user_menu()
        if action.upper() == 'V':
            view_an_item()
        elif action.upper() == 'A':
            add_item_to_menu()
        elif action.upper() == 'D':
            remove_item_from_menu()
        elif action.upper() == 'U':
            update_item_from_menu()
        elif action.upper() == 'S':
            show_restaurant_menu()
        elif action.upper() == 'X':
            in_user_menu = False
        else:
            print("\nUnfortunately, your input doesn't exist in our program.")


menu_editor()