print("Enter Marks Obtained in 5 Subjects:")

math = int(input())
physics = int(input())
chemistry = int(input())
biology = int(input())
social = int(input())
hindi = int(input())
french = int(input())
Ict = int(input())

total = math + physics + chemistry + biology + Ict + social + hindi + french
avg = int(total / 8)

validRange = range(0, 100)


if avg in range(91, 100):
    print("Your Grade is A1")

elif avg in range(81, 91):
    print("Your Grade is A2")

elif avg in range(71, 81):
    print("Your Grade is B1")

elif avg in range(61, 71):
    print("Your Grade is B2")

elif avg in range(51, 61):
    print("Your Grade is C1")

elif avg in range(41, 51):
    print("Your Grade is C2")

elif avg in range(33, 41):
    print("Your Grade is D")

elif avg in range(21, 33):
    print("Your Grade is E1")

elif avg in range(0, 21):
    print("Your Grade is E2")
else:
    print("u need to go back to kindergarden")