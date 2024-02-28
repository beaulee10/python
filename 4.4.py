POUND = 0.453592
INCH = 0.0254

weight = float(input("Enter your weight in pounds: "))
height = float(input("Enter your height in inches: "))

kilograms = POUND * weight
meters = INCH * height

bmi = kilograms / (meters * meters)
print(f"Your bmi is {bmi}")

if (bmi < 18.5):
    print("You are in the underweight category.")
elif(18.5 <= bmi <= 24.9):
    print("You are in the normal weight category.")
elif(25 <= bmi < 29.9):
    print("You are in the overweight category.")
elif(bmi >= 30):
    print("You are in the obese category.")
