from cxxulib.printer import print1
from user.models import User

uob=User.objects
users=uob.all()
print1(users)
user1=uob.get(11)