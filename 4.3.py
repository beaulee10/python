def calculated_interest(principal, rate, time):
    simple_interest = (principal*rate*time)/100
    return simple_interest

input_principal = float(input("Enter the principal rate: "))
input_rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
input_time = float(input("Enter the investment time in whole years: "))

result = calculated_interest(principal=input_principal, rate=input_rate, time=input_time)
print(f"The simple interest for a principal amount of ${input_principal:,.2f} at an interest rate of {input_rate}% over a period of {input_time} years is: ${result:,.2f}")