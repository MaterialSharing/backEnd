from datetime import timedelta, datetime

from django.utils import timezone

d = {"hours": 5}
now = datetime.now()
print("@now:", now)
delta = timedelta(**d)
print(delta)
time_range_start = now - delta

#
print("@time_range_start:", time_range_start)
