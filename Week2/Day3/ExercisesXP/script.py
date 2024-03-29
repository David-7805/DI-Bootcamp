from string import ascii_letters
from random import choices
import datetime
from faker import Faker

# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}s'

    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.amount} {self.currency}s'

    def __add__(self, other):
        if type(other) == Currency:
            if self.currency == other.currency:
                return self.amount + int(other)
            else:
                raise TypeError(f"Cannot add between currency types {self.currency} and {other.currency}.")
        elif (type(other) == int) or (type(other) == float):
            return self.amount + other

    def __iadd__(self, other):
        if type(other) == Currency:
            if self.currency == other.currency:
                self.amount = self.amount + other.amount
            else:
                raise TypeError(f"Cannot add between currency types {self.currency} and {other.currency}.")
        elif (type(other) == int) or (type(other) == float):
            self.amount = self.amount + other
        return self



c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)
print(c1)
c1 += 5
print(c1)
c1 += c2
print(c1)
# print(c1 + c3)

# Exercise 3: String Module
# 1.
print(ascii_letters)
list_of_five_random_letters = choices(ascii_letters, k = 5)
random_string_of_5 = ''.join(list_of_five_random_letters)
print(random_string_of_5)

# Exercise 4: Current Date
def current_date():
    current_date = datetime.date.today()
    print(current_date)

current_date()

# Exercise 5: Amount Of Time Left Until January 1st
def time_to_new_year(year):
  any_new_year = f'{year}-01-01 00:00:00'
  any_new_year_datetime_object = datetime.datetime.strptime(any_new_year, "%Y-%m-%d %H:%M:%S")
  now = datetime.datetime.now()
  time_to_new_year = str(any_new_year_datetime_object - now) # returns a string like '294 days, 2:09:26.596043'
  list_of_time_to_new_year = time_to_new_year.split(', ')
  list_of_time_to_new_year[1] = list_of_time_to_new_year[1].split('.') # I want to get rid of the decimals after the '.'
  print(f'The 1st January of {year} is in {list_of_time_to_new_year[0]} and {list_of_time_to_new_year[1][0]} hours.')

time_to_new_year(2025)
time_to_new_year(2026)

# Exercise 6 : Birthday And Minutes
def minutes_lived(birth_year, birth_month, birth_day):
    birth_date = datetime.date(birth_year, birth_month, birth_day)
    current_date = datetime.date.today()
    time_lived = current_date - birth_date
    list_of_time_lived = str(time_lived).split(' ') # String '16739 days, 0:00:00' is being split, I only need the first part
    days_lived = int(list_of_time_lived[0])
    minutes_lived = days_lived * 24 * 60
    print(f"You have lived approximately {minutes_lived} minutes until this date.")

minutes_lived(1978, 5, 14)

# Exercise 7 : Faker Module
def fake_persons_creator(amount):
    locale_list = ['he', 'en_US', 'en_GB', 'es_MX', 'de', 'fr', 'ru']
    users = []
    for number in range(10):
        locale = choices(locale_list, k = 1)
        fake = Faker(locale)
        dict_of_fake_persons = {}
        dict_of_fake_persons['name'] = fake.name()
        dict_of_fake_persons['address'] = fake.address()
        dict_of_fake_persons['language code'] = locale
        users.append(dict_of_fake_persons)
    return users

print(fake_persons_creator(10))





