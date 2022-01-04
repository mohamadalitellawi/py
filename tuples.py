stats = (48.0,30.5,20.2,100.0,48.0)
herbs = ("lavender", "pokeroot", "chamomile", "valerian","nettles", "oatstraw")
movie = ("Monty Python",1975,9.99)
scores = (99,)

i,j,l,m,n = stats
print(i)

def get_location():
    return 0, 0 , 0

print(get_location())
print(scores[0])

print(5/2,5//2,5%2)

t = (n*n*n//9 for n in stats)
print(tuple(t))