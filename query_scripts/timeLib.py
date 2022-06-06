from datetime import timedelta, datetime,date

from django.utils import timezone
today_date=date.today()
print("@today_date", today_date)
date_turned=date.fromisoformat("2023-08-15")
print("@date_turnd", date_turned,type(date_turned))

delta_time=date_turned-today_date
print("@delta_time", delta_time)
print("@delta_time:days:", delta_time.days)

# -------------
d = {"hours": 5}
now = datetime.now()
print("@now:", now)
delta = timedelta(**d)
print(delta)
time_range_start = now - delta
# print("type of time_range")
#
print("@time_range_start:", time_range_start)
