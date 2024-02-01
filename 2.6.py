# Each category will ask the user how much they spend on each category
Housing = float(input("How much does your housing (rent or mortgage) cost? "))
Utilities = float(input("How much does your utilities cost? "))
Groceries = float(input("How much does your grocerries cost? "))
Transportation = float(input("How much does your transportation cost? "))
HealthCare = float(input("How much does your health care cost? "))
PersonalCare = float(input("How much does your personal care cost? "))
Clothing = float(input("How much does your clothing cost? "))
Debt = float(input("How much does your debt cost? "))
# This equation below will total all the total cost 
Total = (Housing + Utilities + Groceries + Transportation + HealthCare + PersonalCare + Clothing + Debt)
# Each print function will display the percentage each category makes up
# The equation at the end of each print function calculates the percentage for each category
print(f"Your housing budget is {(Housing / Total) * 100 :.2f}%")
print(f"Your utilities budget is {(Utilities / Total) * 100 :.2f}%")
print(f"Your groceries budget is {(Groceries / Total) * 100 :.2f}%")
print(f"Your transportation budget is {(Transportation / Total) * 100 :.2f}%")
print(f"Your health care budget is {(HealthCare / Total) * 100 :.2f}%")
print(f"Your personal care budget is {(PersonalCare / Total) * 100 :.2f}%")
print(f"Your clothing budget is {(Clothing / Total) * 100 :.2f}%")
print(f"Your debt budget is {(Debt / Total) * 100 :.2f}%")
