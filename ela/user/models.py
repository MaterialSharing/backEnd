# from doctest import Example
# from pyexpat import model
# from email.policy import default
from django.db import models
import random as rand

# Create your models here.
from django.forms import forms


class User(models.Model):
    uid = models.AutoField(primary_key=True,help_text="Unique ID")
    name = models.CharField(max_length=50, default='name_id',help_text="User's name")
    signin = models.IntegerField(db_column='signIn', default=0,
                                 help_text="the sign in days >=0")  
    openid = models.CharField(max_length=150, null=True, default=None, unique=True,help_text="User's openid")
    examdate = models.DateField(db_column='examDate', default='1970-01-01',help_text="User's exam date")
    signupdate = models.DateField(db_column='signUpDate', auto_now_add=True,help_text="User's sign up date")

    # signupdate = models.DateField(db_column='signUpDate', default='1970-01-01')  
    # 使用微信授权登录,不设密码字段?
    # password = models.CharField(default="123",widget=forms.PasswordInput, max_length=20)

    # test=models.IntegerField(default=0)
    class Meta:
        managed = True
        db_table = 'user'

    def __str__(self):
        s = self
        return str([s.uid, s.name, s.signin, s.examdate, s.examtype, s.signupdate])

    # @property
    # def user_name(self):
    #     s = self
    #     return s.name
    # @property
    def alias(self):
        # return [1,3,4]
        # print( "@uws.values():",self.user_word_star.values())
        # 返回全部字段
        # print(self.user_word_star.values())
        return self.user_word_star.values("spelling", "id")
        # return self.user_word_star.values()


# class UserInfo(models.Model):
#     # 使用默认值会优于可空值(如果能够找到合适的more值的话!)
#     # 默认值是仅在django中体现的吗?(估计是)
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  
#     examtype = models.CharField(db_column='examType', max_length=1,default=4)  
#     examdate = models.DateField(db_column='examDate',default='1970-01-01')  
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  
#
#     class Meta:
#         managed=True
#         db_table = 'user_info'
# class U(models.Model):
#     # 使用默认值会优于可空值(如果能够找到合适的more值的话!)
#     # 默认值是尽在django中体现的吗?(估计是)
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  
#     examtype = models.CharField(db_column='examType', max_length=1,default=4)  
#     examdate = models.DateField(db_column='examDate',default='1970-01-01',null=True)  
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  
#
#     class Meta:
#         managed=True
#         db_table = 'U'
# class User(models.Model):
#     uid = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=20,default='name_id')
#     signin = models.IntegerField(db_column='signIn',default=0)  
#     examtype = models.CharField(db_column='examType', max_length=1)  
#     examdate = models.DateField(db_column='examDate',default='1970-01-01')  
#     signupdate = models.DateField(db_column='signUpDate',default='1970-01-01')  
#
#     class Meta:
#         managed=True
#         db_table = 'user'

class WordStar(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_word_star", db_constraint=False)
    spelling = models.CharField(default="application", max_length=25)

    # testField=models.CharField(default="testField",max_length=55)
    class Meta:
        managed = True
        db_table = 'word_star'
        # unique_together = (('uid', 'spelling'),)

    def __str__(self):
        s = self
        return str([s.id, s.user, s.spelling])
        # return "ws@@"

    #     自定义属性方法
    # @property
    # def spelling(self):
    #     return [12, 3, 4]
    # return self.spelling.Upper()
    # return self.user_id.values()
    #     # print(self.user_word_star)
    # return User.objects.values()
    @property
    def alias(self):
        return [1, 2, 3]


class WordSearchHistory(models.Model):
    # 主键不显示设置,django自动生成
    # 将uid设置为外键.
    # user = models.IntegerField()
    # 将外键行设置为虚拟外键(db_constraint=False)
    class Meta:
        managed = True
        db_table = 'word_search_history'
        # unique_together = (('uid', 'spelling'),)

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_search_history", db_constraint=False)
    spelling = models.CharField(default="application", max_length=25)

    def __str__(self):
        s = self
        return str([s.id, s.user, s.spelling])
    # def ush(self):
    #     return self.user_search


class TestForeignKey(models.Model):
    # 外键会实际的在数据库中生成
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_testF", db_constraint=False)
    count = models.CharField(max_length=50)
    #     如果不设置Meta,数据库名称将自动生成


class FeedBack(models.Model):
    # uid = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_feedback", db_constraint=False)
    content = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'feed_back'
