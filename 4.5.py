def factorial(n, base = 1):
    if n > 1:
        return factorial(n-1, base*n)
    else:
        return base

def main():
     n = int(input("Enter a non-negative number: "))
     result = factorial(n)
     print(f"The factorial of {n} is {result}.")

main()