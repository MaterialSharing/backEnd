from blogs.models import Blog
""" 一对多:ForeignKey:作用于主表"""
# blog是外键(是Entry模型(主表)中引用Blog模型(外表)的一个字段)
# 一个简单的例子是:一个主人-宠物关联模型:宠物模型中定义了主人字段(通过外键的方式参考于主人表)
# 一个主人可以有多个宠物,而主人想要查询他的所有宠物,可以通过虚拟的关联字段来查询(反向查询)
#django能够做到反向引用(即,通过外表直接知道是哪个表引用了自己,这种关联访问的效果就仿佛是该虚拟字段如同真的定义在了外表一般
blog = Blog.objects.get(id=1)
blog.entry_set.all()  # Returns all Entry objects related to Blog.

# b.entry_set is a Manager that returns QuerySets.
blog.entry_set.filter(headline__contains='Lennon')
blog.entry_set.count()
# 通过idea的intellisense可以提示反向关联!
# blog.
# 你可以在定义 ForeignKey 时设置 related_name 参数重写这个 FOO_set 名。
# 例如，若修改 Entry 模型为 blog = ForeignKey(Blog, on_delete=models.CASCADE, related_name='entries')，前文示例代码会看起来像这样:
blog = Blog.objects.get(id=1)
blog.entries.all() # Returns all Entry objects related to Blog.

# b.entries is a Manager that returns QuerySets.
blog.entries.filter(headline__contains='Lennon')
blog.entries.count()
""" 多对多:ManyToMany(学生-课程模型)"""
# 和 ForeignKey 类一样，你也可以创建 自关联关系 （一个对象与他本身有着多对多的关系）和 与未定义的模型的关系 。
#
# 建议设置 ManyToManyField 字段名（上例中的 toppings ）为一个复数名词，表示所要关联的模型对象的集合。
#
# 对于多对多关联关系的两个模型，可以在任何一个模型中添加 ManyToManyField 字段，但只能选择一个模型设置该字段，即不能同时在两模型中添加该字段。
# 一般来讲，应该把 ManyToManyField 实例放到`需要在表单中被编辑的对象`中。
# 在之前的例子中， toppings 被`放在` Pizza 当中
#   （而不是 Topping 中有`指向` pizzas 的 `ManyToManyField 实例 `）
# 因为相较于配料被放在不同的披萨当中，`披萨当中有很多种配料`更加符合常理.