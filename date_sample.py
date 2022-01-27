from datetime import date
from datetime import time
from datetime import datetime

from datetime import date, time, datetime, timedelta

d1 = date.today()

d2 = time(1,2,10,50)
d3 = datetime.today()

d4 = datetime.strptime("220123","%y%m%d")
print (d1, d2)
print(d4)

print(f"Date formatted: {d3:%d-%m-%Y}")

td = timedelta(weeks=2,hours=12)
print(td.total_seconds()/3600.0/24)

d5 = d3+td
print(type(d5))

print(datetime.today().year)