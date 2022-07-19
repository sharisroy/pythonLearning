mark = int(input("Enter a number(0 to 100) for check Grade: "))
if mark >= 0:
    if mark >= 80:
        print("A+")
    elif mark >= 70:
        print("A")
    elif mark >= 60:
        print("B")
    elif mark >= 50:
        print("C")
    else:
        print("Fail")
else:
    print("Invalid Number")

#  Find large Number among three numbers
print("Find large Number among three numbers")
a = int(input("Enter 1st Number: "))
b = int(input("Enter 2nd Number: "))
c = int(input("Enter 3rd Number: "))

if a > b:
    if a > c:
        print("1st Number is large")
    else:
        print("3rd Number is large")
else:
    if b > c:
        print("2nd Number is large")
    else:
        print("3rd Number is large")