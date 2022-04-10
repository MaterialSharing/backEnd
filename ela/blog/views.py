from django.http import HttpResponse
from blog.models import Blog, Entry

def index(request):
    # 添加一个对象(一行记录)
    b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
    # 调用实例的save()来保存到数据库
    b.save()
    # 使用模型管理器来直接create(insert一条记录)
    b = Blog.objects.create(name='Cheddar Talk', tagline='All the latest Beatles news.')
    Eob=Entry.objects
    Eob.create()

    
    # 分别获得两个表的一个对象
    entry = Entry.objects.get(pk=1)
    cheese_blog = Blog.objects.get(name="Cheddar Talk")
    # 利用外键对象修改主键对象的一个字段(这个字段的类型就是外键模型)
    # 
    entry.blog = cheese_blog
    entry.save()
    print(type(entry.blog),type(cheese_blog))
    return HttpResponse(entry.blog)