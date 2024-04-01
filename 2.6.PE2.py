def main():
    list = []
    print("Please enter names of flowers then type 'done' when finished:")
    while True:
        flower = input().strip().lower()
        if flower == 'done':
            break
        list.append(flower)

    list.sort()

    print("List of Flowers:")
    for i, flower in enumerate(list, start=1):
        print(f"{i}. {flower}")

    sort_flowers = input("Enter a flower to search: ").strip().lower()
    if sort_flowers in list:
        print(f"{sort_flowers.capitalize()} is not on the list.")
    else:
        print(f"{sort_flowers.capitalize()} is not on the list.")

    try:
        number = int(input("Type a number to get a correlating flower: ")) - 1
        if number < 0 or number >= len(list):
            raise IndexError
        print(f"The flower at position {number + 1} is {list[number].capitalize()}.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except IndexError:
        print("Invalid number. Please enter a number within the range of the list.")
    except:
        print("An error occurred:")

main()
