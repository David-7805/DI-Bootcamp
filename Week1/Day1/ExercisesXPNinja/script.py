# Exercise 3
def predict(statement, prediction):
    if statement == prediction:
        print(f"{prediction} was the right prediction")

predict(3 <= 3 < 9, True)
predict(3 == 3 == 3, True)
predict(bool(0), False)
predict(bool(5 == "5"), False)
predict(bool(4 == 4) == bool("4" == "4"), True)
predict(bool(bool(None)), False)

x = (1 == True)
y = (1 == False)
a = True + 4 # a == 5
b = False + 10 # b == 10

predict(x, True)
predict(y, False)

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

# Exercise 4

my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
print(len([character for character in my_text if character != ' ']))

# Exercise 5

record = 0
while True:
    attempt = input("Make the longest sentence you can without using the character a, or type q to quit:")
    if attempt == 'q':
        break
    elif 'a' in attempt or 'A' in attempt:
        print("Your sentence is invalid as it contains an a.")
    elif len(attempt) <= record:
        print("Your sentence is valid, but unfortunately not longer than a previous one.")
    else:
        print(f"Congratulations! You set a new longest sentence without an a. The record sentence is \n{attempt}")
        record = len(attempt)