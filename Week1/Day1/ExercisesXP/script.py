print("Hello world\nHello world\nHello world\nHello world")

some_math = (99 ** 3) * 8
print(some_math)

def predict(statement, prediction):
    if statement == prediction:
        print(f"{prediction} was the right prediction")

predict(5 < 3,False)
predict(3 == 3, True)
predict(3 == "3", False)
# "3" > 3 It is impossible to perform the greater than operator on a string and an integer
predict("Hello" == "hello", False)

computer_brand = "Acer"
print(f'I have an {computer_brand} computer')
