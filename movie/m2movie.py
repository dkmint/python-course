from m2modlist import *

movie_list = [["Monty Python and the Holy Grail", 1975],
              ["On the Waterfront", 1954],
              ["Cat on a Hot Tin Roof", 1958]]

display_menu()

while True:
    command = input("Command: ")
    if command.lower() == 'list':
        list(movie_list)
    elif command.lower() == 'add':
        add(movie_list)
    elif command.lower() == 'del':
        delete(movie_list)
    elif command.lower() == 'exit':
        break
    else:
        print("Not a valid command. Please try again.\n")

print("Bye!")
