import calendar
import datetime

def main():
    current_year = datetime.datetime.now().year
    
    month_of_birth = input("Enter the number that represents your birth month (like January as 1, Feburary as 2< etc.): ")
    
    try:
        month_of_birth = int(month_of_birth)
        
        if month_of_birth < 1 or month_of_birth > 12:
            print("Invalid input. Please enter a month between 1 and 12.")
            return
        
        print(calendar.month(current_year, month_of_birth))
    
    except ValueError:
        print("Invalid input. Please enter a valid integer for the month.")

main()