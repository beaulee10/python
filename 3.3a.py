integer = int(input("Enter an  integer: "))
integer2 = int(input("Enter another integer: "))

if integer > 0 and integer2 > 0:
    print("Both numbers are greater than 0: True")
else:
    print("Both numbers are greater than 0: False")
if integer > 100 and integer2 > 100:
    print("Both numbers are greater than 100: True")
else:
    print("Both numbers are greater than 100: False")

if (integer % 2) == 0 or (integer2 % 2) == 0:
    print("Either number is even? True")
else:
    print("Either number is even? False")
if integer < 100 or integer2 < 100:
    print("Either number is less than 100? True")
else:
    print("Either number is less than 100? False")

if not integer == integer2:
    print("num1 is not equal to num2:  True")

if not integer == 1:
    print("num1 is not 0:  True")