l = list(range(21))
print(l)

l2 = [x*2 for x in l if x%3 == 0]

#print(l2)

def square(n):
    return n * n
def is_even(n):
    return n%2 == 0

l3 = [square(n) for n in l if is_even(n)]
#print (l3)


import random
def get_random_num():
    return random.randrange(1,10)

l4 = [square(num) for n in range(20) if (num:= get_random_num()) <= 6]

print (l4)