from m4modlist import *

display_menu()
movies = read_movies()
while True:
    command = input('Command: ')
    if command == 'list':
        list_movies(movies)
    elif command == 'add':
        add_movie(movies)
    elif command == 'del':
        delete_movie(movies)
    elif command == 'exit':
        print('Bye!')
        break
    else:
        print('Not a valid command. Please try again.')
