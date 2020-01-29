from m3modlist import *

movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
              ["On the Waterfront", 1954, 5.59],
              ["Cat on a Hot Tin Roof", 1958, 7.95]]
#year = input("Enter Year: ")
#year = int(year)
#for i in movie_list:
#    for j in i:
#        if j == year:
#            s = i[0:1]
#            print('  '.join(s) + ' was released in ' + str(year))

display_menu()

while True:
    command = input("Command: ")
    if command.lower() == 'list':
        list(movie_list)
    elif command.lower() == 'add':
        add(movie_list)
    elif command.lower() == 'del':
        delete(movie_list)
    elif command.lower() == 'find':
        find(movie_list)
    elif command.lower() == 'exit':
        break
    else:
        print("Not a valid command. Please try again.\n")

print("Bye!")
