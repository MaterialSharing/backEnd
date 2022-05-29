import hashlib

from django.contrib.auth.hashers import make_password

from cxxulib.printer import print1
from cxxulib.static_values import uob
from user.models import User
from user.serializer import UserModelSerializer

# uob=User.objects
# users=uob.all()
# print1(users)
# user1=uob.get(pk=11)

data = {"name": "by_data", "signin": 101}
ser = UserModelSerializer(data=data)
ser.is_valid(raise_exception=True)
data["password"] = "123"
data["password2"] = "123"
# password_hash=make_password("123")
# password_hash2=make_password("123")
md5 = hashlib.md5()
user = uob.filter(name='cxxu').first()
# 获取用户输入的密码以及用户的干扰盐(得到salt_password)
salt_password = user.password_salt + "123"
# 将利用md5对象的update方法对字符串加密
md5.update(salt_password.encode('utf-8'))
password_hash_wait = md5.hexdigest()
print("@password_hash:", password_hash)
print("@password_hash2:", password_hash2)
ser.data

ser.save()
ser.data
