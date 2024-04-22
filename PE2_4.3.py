def main():
    total = 0
    count = 0
    
    try:
        with open("sales_totals.txt", 'r') as file:
            for accounts in file:
                try:
                    number = float(accounts.rstrip())
                    total += number
                    count += 1
                    print(f"{number:,.2f}")
                except ValueError:
                    print("Error: Invalid number format.")
        
        print(f"Total: {total:,.2f}")
        print(f"Count: {count}")
        if count > 0:
            print(f"Average: {total / count:,.2f}")
        else:
            print("No entries found.")
    except IOError:
        print("An IOError has occurred.")

main()
