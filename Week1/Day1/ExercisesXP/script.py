# Exercise 1
print("Hello world\n" * 4)

# Exercise 2
some_math = (99 ** 3) * 8
print(some_math)

# Exercise 3
def predict(statement, prediction):
    if statement == prediction:
        print(f"{prediction} was the right prediction")
    else:
        print(f"{prediction} was the wrong prediction")

predict(5 < 3, False)
predict(3 == 3, True)
predict(3 == "3", False)
# "3" > 3 It is impossible to perform the greater than operator on a string and an integer
predict("Hello" == "hello", False)

# Exercise 4
computer_brand = "Acer"
if computer_brand[0] in 'AEIOYaeioy':
    print(f'I have an {computer_brand} computer')
else:
    print(f'I have a {computer_brand} computer')

# Exercise 5
name = "David"
age = 45
shoe_size = 44
info = f'Hi, my name is {name}, I am {age} years old. For those who want to know, my shoe size is {shoe_size} : )'
print(info)

# Exercise 6

a = 28
b = 14
if a > b:
    print("Hello World")

# Exercise 7
given_number = input("Please enter a number: ")
if int(given_number) % 2 == 0:
    print("You entered an even number")
else:
    print("You entered an odd number")

# Exercise 8
name_entered = input("Please enter your name: ")
if name_entered == "David":
    print(f"What a coincidence, my name is {name_entered} too!")
else:
    print(f'{name_entered} is a nice name too!')

# Exercise 9
height = input("Please enter your height in cm: ")
if int(height) > 145:
    print("You are tall enough to ride : )")
else:
    print("You need to grow some more to ride")

