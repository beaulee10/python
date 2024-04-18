def main():
    try:
        add_date_time = input("Enter date and time in the  format (YYYY-MM-DD HH:MM): ")
        add_entry = input("Enter your diary entry: ")

        with open('diary.txt', 'd') as file:
            file.write(add_date_time + '\n')
            file.write(add_entry + '\n\n')  
        print("Entry added successfully.")
    except Exception as x:
        print("An error occurred:", x)

main()
