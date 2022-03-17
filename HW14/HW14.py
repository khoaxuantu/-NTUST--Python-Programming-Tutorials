# Address Book

def main():
    add_book = {}
    # Set up options
    print("** Address Book **")

    print("1. Create a New Contact")
    print("2. Look up the Telephone by Name")
    print("3. Look up the Name by Telephone")
    print("4. List the Whole Address Book")
    print("5. Quit")
    print()

    while True:
        # Enter a choice
        choice = int(input("Please enter your choice: "))

        # Implement each choice
        if choice == 1:
            name = input("Please enter the name: ")
            phone_num = input("Please enter the phone: ")
            add_book[name] = phone_num
        elif choice == 2:
            name = input("Please enter the name to look up telephone: ")
            print(f"Search result: {lookup_byname(name, add_book)}")
        elif choice == 3:
            phone_num = input("Please enter the phone to look up name: ")
            print("Search result:")
            lookup_bytel(phone_num, add_book)
        elif choice == 4:
            for name in add_book:
                print("{}{:>8}{}".format(name, ":", add_book[name]))
        else:
            print("Thanks for your use!")
            break
        print()


# Looking up telephone number by name
def lookup_byname(string, add_book):
    for name in add_book:
        if string not in add_book:
            print("Not found!")
        elif name == string:
            return add_book[name]


# Looking up name by telephone number
def lookup_bytel(number, add_book):
    found = False
    for name in add_book:
        if add_book[name] == number:
            print("{}{:>8}{}".format(name, ":", add_book[name]))
            found = True
    if found is False:
        print("Not found!")


if __name__ == "__main__":
    main()
