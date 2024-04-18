from Management import LibraryOperations, username

library_operations = LibraryOperations()

def welcome_page():
    while True:
        try:
            welcome_input = int(input(f"\nWhat would you like to do, {username}?\n\t1. Book Operations\n\t2. User Operations\n\t3. Author Operations\n\t4. Quit\n\t\t{username}: "))
            if isinstance(welcome_input, int):
                if welcome_input == 4:
                    break
                elif welcome_input == 1:
                    library_operations.set_book_operations()
                elif welcome_input == 2:
                    library_operations.set_user_operations()
                elif welcome_input == 3:
                    library_operations.set_author_operations()
            else:
                print("\nPlease enter a valid number.")
        except ValueError:
            print("Please enter a number")

welcome_page()

print("Thanks for using JLRA! Have a good day! :)")
