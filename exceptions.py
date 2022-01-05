from typing import cast


'''
try:
    num = int(input("Inter number: "))
    print(f"ok {num}")
except ValueError:
    print("no")

print()
print("thanks")

'''

def func():
    pass

a = 5
b = (0,0,0)
c = [0,0,0]
d = {}
print(type(list))
print(type(func))
print(type(a))
print(type(b))
print(type(c))
print(type(d))


import sys
filename = "test.txt"
movies = []
try:
    with open(filename) as f:
        for line in f:
            line.replace("\n","")
            movies.append(line)
    print(movies)
    raise OSError("Start the fight")
except FileNotFoundError as e:
    print("File Not found Error: ", e)
    print(type(e),":", e)
    sys.exit()
except OSError as e:
    print("OSError: ", e)
    print(type(e),":", e)
    sys.exit()
except Exception as e:
    print(type(e),":", e)
    sys.exit()
