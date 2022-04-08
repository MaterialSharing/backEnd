from myapp.models import User

mod=User.objects
l=mod.all()
for item in l:
    print(item)