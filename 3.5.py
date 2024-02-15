# Initialize a list of names
names = []

name1 = input("Give me a name : ")
names.append(name1)
name2 = input("Give me another name : ")
names.append(name2)
name3 = input("Give me another name : ")
names.append(name3)
name4 = input("Give me another name : ")
names.append(name4)
name5 = input("Give me another name : ")
names.append(name5)

# Flag to track if a swap has occurred
swapped = True

# make all names lower case

for i in range(0, len(names)):
    names[i] = names[i].lower()

# Continue looping until no swaps occur
while swapped:
    swapped = False  # Reset the flag at the start of each iteration
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # A swap is needed
            # Swap the elements
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print(names)

# Reverse the list
names.reverse()

# Print the reversed list
print(names)