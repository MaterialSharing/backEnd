from cxxulib.printer import print1
from user.models import User
from user.serializer import UserModelSerializer

uob=User.objects
users=uob.all()
print1(users)
user1=uob.get(pk=11)

data={"name":"by_data","signin":101}
ser=UserModelSerializer(data=data)
ser.is_valid(raise_exception=True)
ser.data

ser.save()
ser.data

