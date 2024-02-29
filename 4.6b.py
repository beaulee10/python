nato_alphabet = {
        "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
        "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliet",
        "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
        "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
        "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee", "Z": "Zulu"
    }

def spell_word():
    user_word = input("Enter a word: ").upper()

    for letter in user_word:
        if letter.isalpha():
            print(nato_alphabet.get(letter, letter))
        else:
            print(f"Skipping non-alphabetic character: {letter}")

def main():
    spell_word()

main()