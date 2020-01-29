import pickle

movies = [['Monty Python and the Holy Grsil', 1975],
          ['Cat on a Hot Tin Roof', 1958],
          ['On the Waterfront', 1954]]

with open('movies.bin', 'wb') as file:
    pickle.dump(movies, file)
