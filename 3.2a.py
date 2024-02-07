count = 99
while count >= 3:
    print(count, " Bottles of beer on the wall!")
    print(count, " Bottles of beer!")
    print("Take one down, pass it around!")
    count -= 1  # Increment count
    print(count, " Bottles of beer on the wall!",)
    print("")
 
if count <= 3:
    print(count, " Bottles of beer on the wall!")
    print(count, " Bottles of beer!")
    print("Take one down, pass it around!")
    count -= 1  # Increment count
    print(count, " Bottle of beer on the wall!")
    print("")

if count <= 2:
    print(count, " Bottle of beer on the wall!")
    print(count, " Bottle of beer!")
    print("Take one down, pass it around!")
    count -= 1  # Increment count
    print("No bottles of beer on the wall!")