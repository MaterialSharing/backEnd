from django.db import models
from django.utils import timezone
import datetime
class Question(models.Model):
    # 创建模型字段(映射到数据库表的字段.)
    # 问题内容+发布日期
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # 创建模型函数
    def __str__(self):
        return self.question_text
    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    # 每一个Choice从属于某个问题(question),这里将question配置为Choice的外键(reference)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Choice 文本
    choice_text = models.CharField(max_length=200)
    # 每个choice 获得的票数
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

""" You created a foreign key on Choice which relates each one to a Question.

So, each Choice explicitly has a question field, which you declared in the model.

Django's ORM follows the relationship backwards from Question too, automatically generating a field on each instance called foo_set where Foo is the model with a ForeignKey field to that model.

>>>choice_set is a RelatedManager which can create querysets of Choice objects which relate to the Question instance, e.g. q.choice_set.all()

If you don't like the foo_set naming which Django chooses automatically, or if you have more than one foreign key to the same model and need to distinguish them, you can choose your own overriding name using the related_name argument to ForeignKey. """
    