#The universal conversion variables
global pound, inch
pound = 0.453592
inch = 0.0254

def calculate_bmi(weight, height):
    # Convertion of weight and height to metric units
    kilogram = weight * pound
    meter = height * inch
    
    # Equation/function to calculate BMI
    bmi = kilogram / (meter ** 2)
    return bmi

# This function will determine BMI category the user inputed
def bmi_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif 18.5 <= bmi < 24.9:
        return "normal weight"
    elif 25 <= bmi < 29.9:
        return "overweight"
    else:
        return "obese"

# The main function that executes all the functions to print and calculates statements
def main():
    try:
        weight = float(input("Enter your weight in pounds: "))
        height = float(input("Enter your height in inches: "))
        
        bmi = calculate_bmi(weight, height)
        
        # Shows the results from the user's inputs
        print(f"Your BMI is: {bmi:.2f}")
        print(f"BMI Category: {bmi_category(bmi)}")
    #Will remind and tell the user to enter integers 
    except ValueError:
        print("Cannot enter non-numerical values.")

main()