movies = [["Monty Python and the Holy Grail", 1975], ["Cat on a Hot Tin Roof", 1958], ["On the Waterfront", 1954]]

import pickle
with open("movies.bin","wb") as f:
    pickle.dump(movies,f)

with open("movies.bin","rb") as f:
    movie_list = pickle.load(f)
    print(movie_list)
