s = input("enter string:")
c = input("enter character:")
i = 0
print(len(s))
count = 0
while i < len(s):
    if s[i] == c:
        count += 1
    i+=1
print("there are this many occurrences of the " + c + ":", count) 