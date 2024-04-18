def two_letter(characters):
    for char1 in characters:
        for char2 in characters:
            yield char1 + char2

def main():
    characters = ['a', 'b', 'c']

    print("Combinations for two letters:")
    for combination in two_letter(characters):
        print(combination)

main()
