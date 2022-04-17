# from doctest import Example
# from pyexpat import model
# from email.policy import default
from django.db import models
import random as rand
# Create your models here.

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,default='name_id')
    signin = models.IntegerField(db_column='signIn',default=0)  # Field name made lowercase.
    examtype = models.CharField(db_column='examType', max_length=1,default="4")  # Field name made lowercase.
    examdate = models.DateField(db_column='examDate',default='1970-01-01')  # Field name made lowercase.
    signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  # Field name made lowercase.

    # test=models.IntegerField(default=0)
    class Meta:
        managed=True
        db_table = 'user'

    def __str__(self):
        s=self
        return str([s.uid,s.name,s.signin,s.examdate,s.examtype,s.signupdate])

# class UserInfo(models.Model):
#     # 使用默认值会优于可空值(如果能够找到合适的more值的话!)
#     # 默认值是尽在django中体现的吗?(估计是)
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  # Field name made lowercase.
#     examtype = models.CharField(db_column='examType', max_length=1,default=4)  # Field name made lowercase.
#     examdate = models.DateField(db_column='examDate',default='1970-01-01')  # Field name made lowercase.
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  # Field name made lowercase.
#
#     class Meta:
#         managed=True
#         db_table = 'user_info'
# class U(models.Model):
#     # 使用默认值会优于可空值(如果能够找到合适的more值的话!)
#     # 默认值是尽在django中体现的吗?(估计是)
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  # Field name made lowercase.
#     examtype = models.CharField(db_column='examType', max_length=1,default=4)  # Field name made lowercase.
#     examdate = models.DateField(db_column='examDate',default='1970-01-01',null=True)  # Field name made lowercase.
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  # Field name made lowercase.
#
#     class Meta:
#         managed=True
#         db_table = 'U'
# class User(models.Model):
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  # Field name made lowercase.
#     examtype = models.CharField(db_column='examType', max_length=1)  # Field name made lowercase.
#     examdate = models.DateField(db_column='examDate',default='1970-01-01')  # Field name made lowercase.
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  # Field name made lowercase.
#
#     class Meta:
#         managed=True
#         db_table = 'user'



class WordSearchHistory(models.Model):
    uid = models.IntegerField(primary_key=True)
    spelling = models.IntegerField()

    class Meta:
        managed=True
        db_table = 'word_search_history'
        unique_together = (('uid', 'spelling'),)


class WordStar(models.Model):
    uid = models.IntegerField(primary_key=True)
    spelling = models.IntegerField()

    class Meta:
        managed=True
        db_table = 'word_star'
        unique_together = (('uid', 'spelling'),)
class FeedBack(models.Model):
    uid = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed=True
        db_table = 'feed_back'