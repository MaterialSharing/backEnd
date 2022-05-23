from django.db import models

# Create your models here.
from django.utils import timezone
import datetime

from user.models import User
from word.models import NeepWordsReq, Cet4WordsReq, Cet6WordsReq
from word.serializer import Cet4WordsReqModelSerializer


class NeepStudy(models.Model):
    id = models.AutoField(primary_key=True)
    # wid = models.CharField(max_length=255)
    # wid = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wid = models.ForeignKey(NeepWordsReq, on_delete=models.DO_NOTHING)
    # 在被NeepWordsReq反向引用的时候,默认名虚拟字段名为neepstudy_set;也可以指定related_name
    # DateField.auto_now¶
    # Automatically set the field to now every time the object is saved.
    # Useful for “last-modified” timestamps.
    # last_see_datetime = models.DateTimeField(null=True)
    last_see_datetime = models.DateTimeField(auto_now=True, null=True)
    # 由于此表是学习记录表,所以一定是学习过的单词才会进入到本表中,遂,都是见过面的
    # 自然的,我们可以统计本表中的(指定用户uid,且考试类型:neep类型的)单词的条数,来计算出学习进度.
    # is_new = models.BooleanField(default=True,help_text="单词是否学过")
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    # 通过计算的得到学习进度
    # study_progress = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'neep_study'

    # @property
    def recently(self, days=1):
        now: datetime = timezone.now()  # 类型注解:datatime
        # time_range_start = now - datetime.timedelta(days=1)
        # datetime.timedelta def __new__(cls: Type[Self],
        #             days: float = ...,
        #             seconds: float = ...,
        #             microseconds: float = ...,
        #             milliseconds: float = ...,
        #             minutes: float = ...,
        #             hours: float = ...,
        #             weeks: float = ...) -> Self
        time_range_start = now - datetime.timedelta(days=days)
        time_range_end = now
        # 调用timedelta函数,可以轻松的对某个时间点做偏移
        # python中允许不等式连续拼接
        return time_range_start <= self.last_see_datetime <= time_range_end

    def __str__(self):
        s = self
        return str(
            f"[s.id={s.id}, s.uid={s.user},s.wid={s.wid}, s.last_see_datetime={s.last_see_datetime}, s.familiarity={s.familiarity}]")


class Cet4Study(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wid = models.ForeignKey(Cet4WordsReq, on_delete=models.DO_NOTHING)
    last_see_datetime = models.DateTimeField(auto_now=True, null=True)
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    class Meta:
        managed = True
        db_table = 'cet4_study'

    def __str__(self):
        s = self
        return str(
            f"[s.id={s.id}, s.uid={s.user},s.wid={s.wid}, s.last_see_datetime={s.last_see_datetime}, s.familiarity={s.familiarity}]")

    # 以下属性方法可以再序列化器中使用(显示的声明再field=[]中)
    # 注意,fields="__all__"不会包含这些属性方法
    @property
    def spelling(self):
        return self.wid.spelling

    @property
    def user_name(self):
        return self.user.name

    # @property
    # def wid_obj(self):
    #     # 盗用values()获取字典(而不是queryset)
    #     # return self.wid.values()
    #     # ser=Cet4WordsReqModelSerializer(instance=self.wid).data
    #     # return ser.data
    #     return self.wid.spelling

class Cet6Study(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wid = models.ForeignKey(Cet6WordsReq, on_delete=models.DO_NOTHING)
    last_see_datetime = models.DateTimeField(auto_now=True, null=True)
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    class Meta:
        managed = True
        db_table = 'cet6_study'

    def __str__(self):
        s = self
        return str(
            f"[s.id={s.id}, s.uid={s.user},s.wid={s.wid}, s.last_see_datetime={s.last_see_datetime}, s.familiarity={s.familiarity}]")

    @property
    def spelling(self):
        return self.wid.spelling

    @property
    def user_name(self):
        return self.user.name

class LongSentences(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    contenten = models.CharField(db_column='contentEN', max_length=255)  # Field name made lowercase.
    explaincn = models.CharField(db_column='explainCN', max_length=255, blank=True,
                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'long_sentences'


class ExamReq(models.Model):
    examtype = models.CharField(db_column='examType', primary_key=True, max_length=1)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'exam_req'
