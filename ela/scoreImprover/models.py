from django.db import models

# Create your models here.
class ScoreimproverNeepStudy(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    wid = models.CharField(max_length=255)
    last_see_datetime = models.DateTimeField(blank=True, null=True)
    familiarity = models.IntegerField()
    study_progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scoreimprover_neep_study'
class Cet4WordsReq(models.Model):
    word_rder = models.AutoField(primary_key=True)
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cet4_words_req'


class Cet6WordsReq(models.Model):
    word_order = models.AutoField(primary_key=True)
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cet6_words_req'
class NeepWordsReq(models.Model):
    word_order = models.AutoField(primary_key=True)
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'neep_words_req'
class LongSentences(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    contenten = models.CharField(db_column='contentEN', max_length=255)  # Field name made lowercase.
    explaincn = models.CharField(db_column='explainCN', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'long_sentences'

class ExamReq(models.Model):
    examtype = models.CharField(db_column='examType', primary_key=True, max_length=1)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_req'
