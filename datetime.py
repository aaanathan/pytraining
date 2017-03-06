import datetime

d = datetime.datetime.now()

print d.strftime("%Y-%m-%d %H:%M:%S")

d1 = datetime.date(2017,03,05)
d2 = datetime.date(2017,01,01)

d3 = d1-d2

print d3