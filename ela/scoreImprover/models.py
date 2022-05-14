from django.db import models

# Create your models here.
from user.models import User
from word.models import NeepWordsReq


class NeepStudy(models.Model):
    id = models.AutoField(primary_key=True)  # Field name made lowercase.
    # wid = models.CharField(max_length=255)
    # wid = models.IntegerField(default=0)
    uid = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wid = models.ForeignKey(NeepWordsReq, on_delete=models.DO_NOTHING)
    # 在被NeepWordsReq反向引用的时候,默认名虚拟字段名为neepstudy_set;也可以指定related_name
    # DateField.auto_now¶
    # Automatically set the field to now every time the object is saved.
    # Useful for “last-modified” timestamps.
    # last_see_datetime = models.DateTimeField(null=True)
    last_see_datetime = models.DateTimeField(auto_now=True, null=True)
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    # 通过计算的得到学习进度
    # study_progress = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'neep_study'

    def __str__(self):
        s = self
        return str(
            f"[s.id={s.id}, s.uid={s.uid},s.wid={s.wid}, s.last_see_datetime={s.last_see_datetime}, s.familiarity={s.familiarity}]")


class Cet4Study(models.Model):
    id = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    # wid = models.CharField(max_length=255)
    wid = models.IntegerField(default=0)
    last_see_datetime = models.DateTimeField(blank=True, null=True)
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    class Meta:
        managed = True
        db_table = 'cet4_study'

    def __str__(self):
        s = self
        return str([s.id, s.wid, s.last_see_datetime, s.familiarity, s.study_progress])


class Cet6Study(models.Model):
    id = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    # wid = models.CharField(max_length=255)
    wid = models.IntegerField(default=0)
    last_see_datetime = models.DateTimeField(blank=True, null=True)
    familiarity = models.IntegerField(default=0, help_text="熟练度")

    class Meta:
        managed = True
        db_table = 'cet6_study'

    def __str__(self):
        s = self
        return str([s.id, s.wid, s.last_see_datetime, s.familiarity, s.study_progress])


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
