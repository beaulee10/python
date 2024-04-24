from datetime import datetime

def calculate_age(birth_date):
    current_date = datetime.now()
    
    difference_in_age = current_date - birth_date
    
    age_in_years = difference_in_age.days // 365
    
    leftover_days = difference_in_age.days % 365
    
    age_in_months = leftover_days // 30
    
    leftover_days %= 30
    
    age_in_days = leftover_days
    
    age_in_hours = difference_in_age.seconds // 3600
    age_in_minutes = (difference_in_age.seconds % 3600) // 60
    
    return age_in_years, age_in_months, age_in_days, age_in_hours, age_in_minutes

def main():
    try:
        birth_date_str = input("Enter your birth date in the format(YYYY-MM-DD): ")
        
        birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
        
        age_in_years, age_in_months, age_in_days, age_in_hours, age_in_minutes = calculate_age(birth_date)
        
        print(f"Your age is: {age_in_years} years, {age_in_months} months, {age_in_days} days, {age_in_hours} hours, and {age_in_minutes} minutes.")
    
    except ValueError:
        print("Invalid date format. Enter birth date in YYYY-MM-DD (with dashes '-') format.")

main()
