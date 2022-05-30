## inspecting a Modelserializer

-  [Inspecting a `ModelSerializer`](https://www.django-rest-framework.org/api-guide/serializers/#inspecting-a-modelserializer)

- ModelSerialzier可以用两三行的代码就完成对相应模型的一系列接口

- 这些实现其实最终和手动再Serializer中编写的的一个个声明没差别

- 仅仅是自动生成还是手动编写的差别

- 当然,自动生成的可以通过调用repr来解析序列化器实例看到,是哪些字段被自动生成出来

  - 特别是含有外键模型的时候,这么做又是可以排除故障

  - ```python
    from scoreImprover.serializer import NeepStudyModelSerializer
    
    ser=NeepStudyModelSerializer()
    print(repr(ser))
    # NeepStudyModelSerializer():
    #     id = IntegerField(read_only=True)
    #     last_see_datetime = DateTimeField(read_only=True)
    #     familiarity = IntegerField(help_text='熟练度', max_value=2147483647, min_value=-2147483648, required=False)
    #     user = PrimaryKeyRelatedField(queryset=User.objects.all())
    #     wid = PrimaryKeyRelatedField(queryset=NeepWordsReq.objects.all())
    ```

- [Serializer relations - Django REST framework (django-rest-framework.org)](https://www.django-rest-framework.org/api-guide/relations/)