# from doctest import Example
# from pyexpat import model
# from email.policy import default
from django.db import models
import random as rand
# Create your models here.

class User(models.Model):
    '''自定义Stu表对应的Model类'''
    #定义属性：默认主键自增id字段可不写
    # id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=16)
    # age = models.SmallIntegerField()
    # sex = models.CharField(max_length=1)
    # classid=models.CharField(max_length=8)

    uid= models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    signIn=models.IntegerField(default=0)
    signUpDate=models.DateField()
    examType=models.CharField(max_length=1,default=rand.choice(['4','6','8']))
    examDate=models.DateField(default=f'2022-{rand.randint(1,13)}-18')
    progress4=models.IntegerField(default=0)
    progress6=models.IntegerField(default=0)
    progressNeep=models.IntegerField(default=0)
    progressLongSentence=models.IntegerField(default=0)


    # 定义默认输出格式
    def __str__(self):
        # return "%d:%s:%s:%d"%(self.uid,self.name,self.examDate,self.signIn)
        # return "%d:%s:%d:%s:%s"%(self.id,self.name,self.age,self.sex,self.classid)
        return f'{self.uid},{self.name},{self.examDate},{self.signIn}'


    # 自定义对应的表名，默认表名：myapp_stu
    class Meta:
        db_table="user"


class FeedBack(models.Model):
    uid = models.OneToOneField('User', models.DO_NOTHING, db_column='uid', primary_key=True)  # Field name made lowercase.
    content = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        #managed=False
        db_table = 'feed_back'

class WordSearchHistory(models.Model):
    uid = models.OneToOneField(User, models.DO_NOTHING, db_column='uid', primary_key=True)  # Field name made lowercase.
    spelling = models.ForeignKey('words.Words', models.DO_NOTHING, db_column='spelling')

    class Meta:
        #managed=False
        db_table = 'word_search_history'
        unique_together = (('uid', 'spelling'),)


class WordStar(models.Model):
    uid = models.OneToOneField(User, models.DO_NOTHING, db_column='uid', primary_key=True)  # Field name made lowercase.
    spelling = models.ForeignKey('words.Words', models.DO_NOTHING, db_column='spelling')

    class Meta:
        #managed=False
        db_table = 'word_star'
        unique_together = (('uid', 'spelling'),)
