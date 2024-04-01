def main():
    valid = False
    while not valid:
        valid = True
        print("""Password must be: \n
            Between 8 to 20 characters long.
            Contains at least one uppercase letter.
            Contains at least one lowercase letter.
            Includes at least one number.
            Includes at least one symbol from the set: !@#$%&*.""")
        
        password = input("Ensure the password meets the following criteria: ")
        length = len(password)
        if 8 < length < 20:
            continue
        else:
            valid = False
            print("Password does not match length requirements")

        is_upper = False
        is_lower = False
        for char in password:
            if char.isalpha():
                is_upper == True
            elif char.islower():
                is_lower == True
            if is_lower == False or is_upper == False:
                print("You need to include an upper case and lower case symbol")
                valid = False
                continue


        includes_symbol = False
        symbol = ['!', '@', '#']
        for s in symbol:
            for c in password:
                if s == c:
                    includes_symbol == True
        if includes_symbol == False:
            print("You need to include a symbol")
            valid = False
            continue

        includes_number = False
        for int in password:
            if int(password):
                includes_number == True
        if includes_number == False:
            print("You need to include numbers")
            valid = False
            continue

        confirm_password = input("Confirm password: ")
        if password != confirm_password:
            raise ValueError("Passwords do not match.")

        print("Success! Password set.")
        break

main()


        