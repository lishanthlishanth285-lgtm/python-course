# 1) Display a menu asking the user to select a ride:
#    - 1 for Bike
#    - 2 for Car

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Bike):
#    a) Show bike options (Scooty / Scooter)
#    b) Take the user’s input for bike type and store it in `choice2`
#    c) If `choice2` is 1, print "you have selected scooty"
#       Else, print "you have selected scooter"

# 4) Else if `choice` is 2 (Car):
#    a) Show car options (Sedan / XUV)
#    b) Take the user’s input for car type and store it in `choice3`
#    c) If `choice3` is 1, print "you have selected sedan"
#       Else, print "you have selected XUV"

# 5) Else (if `choice` is not 1 or 2):
#    Print "Wrong choice!"

print("Select a ride:")
print("1 for Bike")
print("2 for Car")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("Select bike type:")
    print("1 for Scooty")
    print("2 for Scooter")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected scooty")
    else:
        print("You have selected scooter")
elif choice == 2:
    print("Select car type:")
    print("1 for Sedan")
    print("2 for XUV")
    choice3 = int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have selected sedan")
    else:
        print("You have selected XUV")
else:
    print("Wrong choice!")