import datetime

now = datetime.datetime.now()
print(now)

today = datetime.date.today()
print(today)

d = datetime.date(2023, 10, 15)  # Example date
print(d)
print(d.strftime("%Y/%m/%d"))