from django.db import models

# Create your models here.
class Words(models.Model):
    spelling = models.CharField(primary_key=True, max_length=255)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    explaincn = models.CharField(db_column='explainCN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    explainen = models.CharField(db_column='explainEN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    plurality = models.CharField(max_length=255, blank=True, null=True)
    pasttense = models.CharField(db_column='pastTense', max_length=255, blank=True, null=True)  # Field name made lowercase.
    presentparticiple = models.CharField(db_column='presentParticiple', max_length=255)  # Field name made lowercase.
    pastparticiple = models.CharField(db_column='pastParticiple', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed=False
        db_table = 'words'
class Cet4WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.ForeignKey('Words', models.DO_NOTHING, db_column='spelling')

    class Meta:
        #managed=False
        db_table = 'cet4_words_req'


class Cet6WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.ForeignKey('Words', models.DO_NOTHING, db_column='spelling')

    class Meta:
        #managed=False
        db_table = 'cet6_words_req'

class NeepWordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.ForeignKey('Words', models.DO_NOTHING, db_column='spelling')

    class Meta:
        #managed=False
        db_table = 'neep_words_req'

class Word_note(models.Model):
    wordspelling = models.CharField(db_column='wordSpelling', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=255, blank=True, null=True)
    difficulty_rate = models.IntegerField(db_column='difficulty_rate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        #managed=False
        db_table = 'word_notes'



