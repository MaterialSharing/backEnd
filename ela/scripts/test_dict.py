from django.test import Client
from django.urls import reverse

client = Client()
# response=client.get('/')

# 借助于命名空间中的定义的name(basename),通过reverse直接访问api
res = client.get(reverse('word:dict', args=['hello']))
res.status_code
data = res.data
content = res.content
type(content)
content.decode('utf-8 ')
