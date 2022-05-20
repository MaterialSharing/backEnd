from django.test import Client
from django.urls import reverse

client = Client()
# response=client.get('/')

# 借助于命名空间中的定义的name(basename),通过reverse直接访问api
# res = client.get(reverse('word:dict', args=['hello']))
# res = client.get(reverse('word:dict'))
# res=client.get('http://127.0.0.1:8000/word/dict/')
# url=reverse('word:dict',args=['apple'])
# url=reverse('word:dict')
# 如果在word的url中使用app_name='word'，则应该使用'word:xx'的形式reverse.
# url=reverse('word:dict_spelling',args=['apple'])
url=reverse('dict_spelling',args=['apple'])
res = client.get('http://127.0.0.1:8000/word/fuzzy/decay/0/')


print(res.status_code)
data = res.data
content = res.content
type(content)
content.decode('utf-8 ')
