# import datetime
from datetime import datetime

today = datetime.now()
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print(today)
print(today.day)
print(today.month)
print(today.weekday())
print(days[today.weekday()])
