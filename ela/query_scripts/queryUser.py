from django.contrib.auth.hashers import make_password

from cxxulib.printer import print1
from user.models import User
from user.serializer import UserModelSerializer

# uob=User.objects
# users=uob.all()
# print1(users)
# user1=uob.get(pk=11)

data={"name":"by_data","signin":101}
ser=UserModelSerializer(data=data)
ser.is_valid(raise_exception=True)
data["password"]="123"
data["password2"]="123"
password_hash=make_password("123")
password_hash2=make_password("123")
print("@password_hash:",password_hash)
print("@password_hash2:",password_hash2)
ser.data

ser.save()
ser.data

