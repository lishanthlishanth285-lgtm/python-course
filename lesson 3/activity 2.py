# 1) Create variables to store different types of values:
#    - `name` as text (string)
#    - `age` as a whole number (integer)
#    - `is_student` as True/False (boolean)
#    - `weight` as a decimal number (float)
# 2) Print each variable’s value.
# 3) Print the datatype of each variable using `type()`.
# 4) Show a message that type casting will happen next.
# 5) Convert `age` from an integer to a string and store it back in `age`.
# 6) Print `age` and print its datatype again to confirm it changed.
# 7) Convert `weight` from a float to an integer and store it back in `weight`.
# 8) Print `weight` and print its datatype again to confirm it changed.

name = "lishanth"

age = 12

is_student = True

weight = 39.8

print("Name =", name, ", Age =", age, ", Is Student =", is_student, ", Weight =", weight)

print(type(name))

print(type(age))

print(type(is_student))

print(type(weight))

print("Type casting will happen next.")

age = str(age)

print(age)

print(type(age))

weight = int(weight)

print(weight)

print(type(weight))

