seats = list(range(1, 21))

while True:
    # Display the list of needed items
        print("Available Seats: ", seats)
        user = input("Enter the seat number you'd like to buy (enter 0 when your done): ")

        if user == "0":
            print("Appreciate your purchase. Enjoy the movie!")
        elif user.isdigit():
            seat_number = int(user)
            if seat_number in seats:
                print(f"You purchased seat {seat_number}.")
                seats.remove(seat_number)
            else:
                print("Invalid seat number or the seat is already purchased. Please choose again.")
        else:
            print("Invalid input. Please enter a valid seat number or try again.")