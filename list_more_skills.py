import copy
import functools

l = [1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)
l.sort()
print(l)

l2 = ["Z","a","c","D","e","f"]
l2.sort(key = str.lower, reverse = True)
print(l2)

mini = min(l2)
print (mini)

print(list(reversed(l + l2)))

l3 = copy.deepcopy(l)

l3[0] = 1000

print(l3[::2])


def squares (n):
    return n *n 

def filter_func (n):
    if n % 3 == 0:
        return True
    return False

l4 = map(squares, l)
l4 = list(l4)
l4.append(1000)

l5 = list(filter(filter_func, l4))
print (l5)

def add_square(total, cuurent):
    return total + (cuurent * cuurent)

total = functools.reduce(add_square,l4)
print(total)