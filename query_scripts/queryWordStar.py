
from cxxulib.printer import print1
from user.models import WordStar
from user.serializer import WordStarModelSerializer

wsob = WordStar.objects
wsall = wsob.all()
# wsall
# 注意关键字参数pk不可以省略
ws1 = wsob.get(pk=2)
# ws1.user
# print(ws1)
data = {"user": 22, "spelling": "apply"}
ser=WordStarModelSerializer(data=data)
ser.is_valid()
ser.data
ser.save()

# ser.data
print1(ser.data)
print("检查ModelSerialzier为我们生成的序列化字段(基于我们指定的数据模型):"
      "检查主表外键关联到外表(模型)的深度(在主表的序列化器的Meta内部类中指定)")
ser=WordStarModelSerializer()
print(repr(ser))
