def replace_artist(top_artists):
    try:
        index = int(input("Enter the index of the artist to replace: "))
        if index < 0 or index >= len(top_artists):
            raise IndexError
        new_artist = input("Enter new name of the artist: ")
        top_artists[index] = new_artist
        print("Artist is now replaced.")
    except (ValueError, IndexError):
        print("An input error occurred.")
    
def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    replace_artist(top_artists)

main()