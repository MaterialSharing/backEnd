from cxxulib.printer import printer1
from user.models import User

uob=User.objects
users=uob.all()
printer1(users)
user1=uob.get(11)