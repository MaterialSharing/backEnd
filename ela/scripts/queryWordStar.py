from cxxulib.printer import printer1
from user.models import WordStar

wsob = WordStar.objects
wsall = wsob.all()
# wsall
# 注意关键字参数pk不可以省略
ws1 = wsob.get(pk=2)
# print(ws1)
printer1(wsall)
