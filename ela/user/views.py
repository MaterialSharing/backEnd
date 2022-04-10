# from django.shortcuts import render
from django.http import HttpResponse
from user.models import User
# from django.urls
# Create your views here.
ob=User.objects
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.\n content provided by poll/view.py")
def userAdd(request,name):
    print("try to add demo user..")
    # 实例化一个新对象,用以增加和修改表的记录
    ob=User()
    # print(ob.objects.all())
    print(ob)
    print(type(ob))
    ob.name=name
    ob.examDate='2021-10-11'
    ob.examType='6'
    ob.signIn=33
    # 使用save执行
    ob.save()
    return HttpResponse(f"{ob.name} added!")

def userDelete(request,name):
    print("try to delete user%s"%(name))
    # t:table
    modUser=User.objects
    user=modUser.all()
def userCheck(request,name):
    print("try user check..")
    ob=User.objects
    try:

        users=ob.all()  
        for user in users:
            print(user)
            print()
        # ob.get(name='cxxu')
        res=ob.get(name=name)
        print(f'@res={res}')
        return HttpResponse(res)
    except:
        return HttpResponse("no specified user exist yet !")
    
