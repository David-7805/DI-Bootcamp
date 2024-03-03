print("Hello world\n" * 4 + "I love python\n" * 4)

given_month = input("Please enter the month (1 to 12): ")
if 3 <= int(given_month) <= 5:
    print("Spring")
elif 6 <= int(given_month) <= 8:
    print("Summer")
elif 9 <= int(given_month) <= 11:
    print("Autumn")
else:
    print("Winter")
