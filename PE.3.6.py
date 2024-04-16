class InvalidInputError(Exception):
    pass

def main():
    while True:
        try:
            user = input("Enter a number: ")
            if not user.isdigit():
                raise InvalidInputError("Invalid input. You need to enter a number.")
        except InvalidInputError as u:
            print(u)
        else:
            print("Valid input:", user)
        finally:
            print("End of code.")


main()
