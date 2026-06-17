number = int(input("Enter a decimal number: "))
binary_string = ""

if number == 0:
    binary_string = "0"

while number > 0:
    remainder = number % 2
    binary_string = str(remainder) + binary_string
    number = number // 2

print("The binary version is:", binary_string)
