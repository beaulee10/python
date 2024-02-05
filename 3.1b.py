#Ask user to input numeric grade
numeric_grade = float(input("Enter numerical grade: "))
#if and elif statement will sort out what numeric grade belongs to each letter grade
if 90 <= numeric_grade <= 100:
        print("A")
elif 80 <= numeric_grade <= 89:
        print("B")
elif 70 <= numeric_grade <= 79:
        print("C")
elif 60 <= numeric_grade <= 69:
        print("D")
elif 0 <= numeric_grade < 60:
        print("F")
#This last line will keep inputs between 0 and 100
else:
    print("Invalid input. Grade must be between 0 and 100.")