POUND = 0.453592 #constant for the pound to kg conversion
INCH = 0.0254 #constant for the inches to meter conversion

weight = float(input("Enter your weight in pounds: ")) #Will ask the user to input their weight in lbs
height = float(input("Enter your height in inches: ")) #will ask user to input their height in inches

kilograms = POUND * weight #This will convert input from pound to kg
meters = INCH * height #This will convert input from inches to meters

bmi = kilograms / (meters * meters) #calculates the BMI
print(f"Your bmi is {bmi}") #prints it

if (bmi < 18.5): #Each if and elif loop will sort out the users calculated BMI to understand and display what weight category they are in
    print("You are in the underweight category.")
elif(18.5 <= bmi <= 24.9):
    print("You are in the normal weight category.")
elif(25 <= bmi < 29.9):
    print("You are in the overweight category.")
elif(bmi >= 30):
    print("You are in the obese category.")
