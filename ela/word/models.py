from django.db import models


# Create your models here.
class Word(models.Model):
    wid = models.AutoField(primary_key=True)
    spelling = models.CharField(max_length=255)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    plurality = models.CharField(max_length=255, blank=True, null=True)
    thirdpp = models.CharField(max_length=255, blank=True, null=True)
    present_participle = models.CharField(max_length=255, blank=True, null=True)
    past_tense = models.CharField(max_length=255, blank=True, null=True)
    past_participle = models.CharField(max_length=255, blank=True, null=True)
    explains = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'words'


class Cet4WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'cet4_words_req'


class Cet6WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'cet6_words_req'


class NeepWordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'neep_words_req'


class WordNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    wordspelling = models.CharField(db_column='wordSpelling', max_length=255, blank=True,
                                    null=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=255, blank=True, null=True)
    difficulty_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'word_notes'
