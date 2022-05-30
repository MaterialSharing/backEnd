from django.contrib import admin

# Register your models here.
# 导入模型,以模型为最小单位想admin注册app中的各个模型
# from .models import ExamReq,LongSentences
from .models import *
admin.site.register([ExamReq ,LongSentences,Cet4Study,Cet6Study,NeepStudy])

