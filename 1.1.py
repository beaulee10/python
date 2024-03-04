import random as r

def main():
    real_number = r.randint(1, 100)

    guess = 0

    try:
        while guess != real_number:
            guess = int(input("Enter a number between 1 and 100: "))

            diff = abs(guess - real_number)

            if diff <= 5:
                print("Very Hot")
            elif diff <= 15:
                print("Hot")
            elif diff <= 25:
                print("Cool")
            else:
                print("Cold")

        print("Congratulations! You have guessed the right number:", real_number)

    except ValueError:
        print("You cannot enter non-numerical inputs")

main()