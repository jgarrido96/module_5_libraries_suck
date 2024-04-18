print('\n')

from newest_library import add_book, add_author, get_author, get_book, get_user, add_user

# Home page

username = input("Welcome, weary traveler, to JDogg's Library for the Reading Abled (JLRA)!\nPlease, enter your name: ")

class LibraryOperations():
    def __init__(self):
        self.book_dict = []
        self.book_borrow = []
        self.user_dict = [username]
        self.author_dict = []
        
        self.book_operations = ()
        self.author_operations = ()
        self.__user_operations = ()

    def get_book_operations(self):
        return self.book_operations

    def set_book_operations(self):
        while True:
            book_input = int(input(f"\nBook operations:\n\t1. Add a new book\n\t2. Borrow a book\n\t3. Return a book\n\t4. Search for a book\n\t5. Display all books\n\t6. Return\n\t\t{username}: "))
            
            if isinstance(book_input, int):
                if book_input == 6:
                    print("Returning to main menu...")
                    break
                
                elif book_input == 1:# add a new book
                    print("\nLet's add some books!\n")
                    title = input("\tEnter the title of the book, or 'return': ")
                    if title == 'return':
                        break
                    else:
                        author = input("\tEnter an Author: ")
                        book = (title, author)
                        if book in self.book_dict:
                            print("This book is already in the library!")
                        else:
                            self.book_dict.append((book))
                            self.author_dict.append(author)
                            add_book(title, author)
                            add_author(author, title)
                            print(f"\n\t{title} by {author} has been added to the library!")
                        
                
                elif book_input == 2:# borrow a book
                    print("\nLet's borrow some books!\n")
                    title = input("\tEnter the title of the book, or 'return': ")
                    if title == 'return':
                        print(self.book_dict)
                        break
                    else:
                        author = input("\tEnter an Author: ")
                        book = (title, author)
                        if book in self.book_borrow:
                            print("This book is already out!")
                        else:
                            if book in self.book_dict:
                                self.book_borrow.append((book))
                                self.book_dict.pop(self.book_dict.index((book)))
                                self.author_dict.pop(self.book_dict.index((author)))
                                print(f"\n\tThanks for checking out {title} by {author}! Please return it in 7 days!")
                            else:
                                print("Sorry! We don't seem to have that title at this time.")


                elif book_input == 3:# return a book
                    return_input = input("What book would you like to return? ")
                    return_author = input("Who's the author? ")
                    return_book = (return_input, return_author)
                    if return_book in self.book_borrow:
                        self.book_borrow.pop(self.book_borrow.index((return_book)))
                        self.book_dict.append((return_book))
                        self.author_dict.append(return_author)
                        print(f"You have succesfully returned {return_input} by {return_author}")
                    else:
                        print("That book hasn't been checked out!\nIf you can't find it, try adding it to the library!")

                elif book_input == 4:# search for a book
                    search_input = input("What book would you like to search for? ")
                    search_author = input("Who's the author? ")
                    book = (search_input, search_author)
                    if book not in self.book_dict:
                        print("We don't seem to have that book.")
                    else:
                        if search_input in self.book_borrow:
                            print("That book is not available!")
                        else:
                            print(f"{search_input} is available for checkout!")

                elif book_input == 5:
                    if self.book_dict == []:
                        print(f"\n\tThere's nothing here yet, {username}!")
                    else:
                        print("\nHere's the what you added to the library:\nTitle:\t\tAuthor:")
                        for book, author in self.book_dict:
                            if len(book) < 10:
                                print(f"{book}\t\t{author}")
                            else:
                                print(f"{book}\t{author}")
                        print(f"\nHere's all the books currently in the library: {get_book()}")

            else:
                print("Please enter a valid input.")
        


    def get_user_operations(self):
        return self.__user_operations

    def set_user_operations(self):
        while True:
            user_input = int(input(f"\nUser operations:\n\t1. Add a new User\n\t2. View User details\n\t3. Display all Users\n\t4. Return\n\t\t{username}: "))
            if isinstance(user_input, int):

                if user_input == 4:
                    print("Returning to main menu...")
                    break

                elif user_input == 1:# add a new user
                    print("\nLet's add some users!\n")
                    username_add = input("\tEnter the name of the user, or 'return': ")
                    if username_add == 'return':
                        break
                    else:
                        if username_add in self.user_dict:
                            print("This User is already accounted for!")
                        else:
                            self.user_dict.append(username_add)
                            books_checked_out = input("How many books have they checked out? ")
                            add_user(username_add, books_checked_out)

                elif user_input == 2:# search for a user
                    search_input = input("Enter the user you'd like to see: ")
                    if search_input not in self.user_dict:
                        print("We don't seem to have that user.")
                    else:
                        if search_input == username:
                            print(f"\n\tStats for {username}:\n\tNumbers of books added:\t{len(self.book_dict)}\n\tNumber of books currently checked out:\t{len(self.book_borrow)}\n\t")
                        else:
                            print(f"\n\tStats for {search_input}:\n\tNumber of books added:\t0\n\tNumber of books currently checked out:\t0")

                elif user_input == 3:
                    if self.user_dict == []:
                        print(f"\n\tThere are no users, {username}!\nWhat a weird enigma!\nCause you're a user.\nSo it's weird that this is showing up.\n\tPLEASE TELL ME HOW YOU DID THIS!!!")
                    else:
                        print("\nHere's are all the users!:\n")
                        for user in self.user_dict:
                            print(f'\t{user}')
            else:
                print("Please enter a valid input.")




    def set_author_operations(self):
        while True:
            author_input = int(input(f"\nAutbor operations:\n\t1. Add a new Author\n\t2. View Author details\n\t3. Display all Authors\n\t4. Return\n\t\t{username}: "))
            if isinstance(author_input, int):

                if author_input == 4:
                    print("Returning to main menu...")
                    break

                elif author_input == 1:# add a new author
                    print("\nLet's add some authors!\n")
                    author = input("\tEnter the name of the author, or 'return': ")
                    if author == 'return':
                        break
                    else:
                        if author in self.author_dict:
                            print("This Author is already accounted for!")
                        else:
                            while True:
                                print("\nLet's add some books!\n")
                                title = input("\tEnter the title of the book, or 'stop' to stop: ")
                                if title == "stop":
                                    break
                                else:
                                    writer = (title, author)
                                    if writer in self.book_dict:
                                        print("This book is already in the library!")
                                    else:
                                        self.book_dict.append((writer))
                                        self.author_dict.append(author)
                                        add_author(author, title)
                                        add_book(title, author)
                                        print(f"\n\t{title} by {author} has been added to the library!")
                
                elif author_input == 2:# search for a user
                    search_input = input("Enter the Author you'd like to see: ")
                    if search_input in self.author_dict:
                        print(f"\n\t{search_input} has books here! If you like their work, go check them out!")
                    else:
                        print(f"That author doesn't have any books here")

                elif author_input == 3:
                    if self.author_dict == []:
                        print(f"\n\tWe don't seem to have any authors here! Add some books and/or authors to see some!")
                    else:
                        print("\nHere's are all the Authors you recently entered:\n")
                        for author in set(self.author_dict):
                            print(f'\t{author}')
                        print("\nThis is a list of every author we have on record:")
                        get_author()
            else:
                print("Please enter a valid input.")

    def get_author_operations(self):
        return self.author_operations

