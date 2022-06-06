```python
def timer_days(self, req):
    sess = req.session
    user = sess.get('cxxu')
    examdate = user.get('examdate')
    # print("@examdate,type",type(examdate))
    # date_obj=date.fromisoformat(examdate)
    # today_date=date.today()
    # delta_time=date_obj-today_date
    # days =delta_time.days

```