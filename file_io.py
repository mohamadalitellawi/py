with open("test.txt","r") as f:
    print(f.readline())

with open("test.txt","a") as f:
    f.write("test\n")

with open("test.txt") as f:
    for line in f:
        print(line,end="")
print()

with open("test.txt") as f:
    print(f.read())

l = range(1,10)
with open("list.txt","w") as f:
    for m in l:
        f.write(f"{m}\n")

members = []
with open("list.txt") as f:
    for line in f:
        line = line.replace("\n","")
        members.append(line)

print(members)

movies = [["Monty Python and the Holy Grail", 1975], ["Cat on a Hot Tin Roof", 1958], ["On the Waterfront", 1954]]
import csv

with open("csv.txt", "w",newline="") as f:
    writer = csv.writer(f)
    writer.writerows(movies)

with open("csv.txt",newline="") as f:
    reader = csv.reader (f)
    for row in reader:
        print(f"{row[0]} ___in the year___ {row[1]}")

print("\n\n\n")

with open("csv.txt", "w",newline="") as f:
    writer = csv.writer(f,delimiter = "\t")
    writer.writerows(movies)

with open("csv.txt",newline="") as f:
    reader = csv.reader (f,delimiter = "\t")
    for row in reader:
        print(f"{row[0]} ___in the year___ {row[1]}")