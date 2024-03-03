entered_string = input("Please enter a string of exactly ten characters: ")
if len(entered_string) < 10:
  print("string not long enough")
elif len(entered_string) > 10:
  print("string too long")
else:
  print("perfect string")

print(entered_string[0], entered_string[-1])

output_string = ''
for letter in entered_string:
  output_string += letter
  print(output_string)