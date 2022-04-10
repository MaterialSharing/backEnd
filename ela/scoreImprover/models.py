from django.db import models

# Create your models here.
class ExamReq(models.Model):
    examtype = models.CharField(db_column='examType', primary_key=True, max_length=1)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)

    class Meta:
        #managed=False
        db_table = 'exam_req'

class LongSentences(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    contenten = models.CharField(db_column='contentEN', max_length=255)  # Field name made lowercase.
    explaincn = models.CharField(db_column='explainCN', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed=False
        db_table = 'long_sentences'

