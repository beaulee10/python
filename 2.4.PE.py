def main():
    books = []

    count = 0
    while count < 10:
        titles = input("Enter book title {}: ".format(count + 1))
        books.append(titles)
        count += 1

    all_sorted_titles = sorted(books)

    print("All book titles sorted:")
    for titles in all_sorted_titles:
        print(titles)

main()

