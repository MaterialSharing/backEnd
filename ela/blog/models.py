from datetime import date

from django.db import models
import random as rand
# from random import random as rand

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    # blog 演示外键(由外键表实例blog查询本表:blog.entry_set...)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    # 演示多对多关系(关联到Author表的)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField(default="blogRand {randint} body contents!".format(randint=rand.randint(1,55)))
    pub_date = models.DateField(default=date.today)
    mod_date = models.DateField(default=date.today)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline


