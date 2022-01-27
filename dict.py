from datetime import datetime as dt
import datetime
import sys

e = dt.today()
l = [1,2,3]
t=(1,2,3)
d = {"a":dt.today(), 
    "b":12563, 
    e:10000000,
    t:l}

print(d[t])

print(e in d.keys())

d[dt.today()] = "Hello"

print(d.get(e + datetime.timedelta(days=2),"None"))

print("_=_"*20)
for x in d:
    print(d[x])

print()
for x,y in d.items():
    print(y)

print()
for x in d.values():
    print(x)

l = [["GB","United kingdom"],
["NL","Netherland"]]

t = (("GB","United kingdom"),
("NL","Netherland"))
print(dict(l),dict(t))

contacts = { 
"Joel":{"address": "1500 Anystreet", "city": "San Francisco", "state": "California", "postalCode": "94110", "phone": "555-555-1111"},
"Anne":{"address": "1000 Somestreet", "city": "Fresno", "state": "California", "postalCode": "93704", "phone": "555-555-2222"},
"Ben":{"address": "1400 Another Street", "city": "Fresno", "state": "California", "postalCode": "93704", "phone": "555-555-4444"}
}

print(contacts["Ben"]["city"])
email = contacts.get("Joel").get("email")
print("0-0"*10,email,"0-0"*10)

students = {"Joel":[85, 95, 70], "Anne":[95, 100, 100], "Mike":[77, 70, 80, 85]}
print(students["Anne"][1])

print(contacts | students)