#Tis will ask user for age 
age = float(input("How old are you? "))
#Will determine if they are old enough to drive
if age >= 16:
    print("You are old enough to drive!")
else:
    print("You are not old enough to drive.")
#Will determine if they are old enough to vote
if age >= 21:
    print("You are old enough to vote!")
else:
    print("You are not old enough to vote.")
#Will determine if they can purchase alcohol
if age >= 21:
    print("You are old enough to legally purchase alcohol!")
else:
    print("You are not old enough to legally purchase alcohol.")
#This will determine if they are eligible for senior dicount
if age>= 65:
    print("You are eligible for senior dicount!")
else:
    print("You are not eligible for senior discount.")
