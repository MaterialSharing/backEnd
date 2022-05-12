from django.db import models


# Create your models here.
class Word(models.Model):
    wid = models.AutoField(primary_key=True)
    spelling = models.CharField(max_length=255)
    phonetic = models.CharField(max_length=255, blank=True, null=True)
    plurality = models.CharField(max_length=255, blank=True, null=True, help_text="noun plural")
    thirdpp = models.CharField(max_length=255, blank=True, null=True, help_text="3rd person present")
    present_participle = models.CharField(max_length=255, blank=True, null=True)
    past_tense = models.CharField(max_length=255, blank=True, null=True)
    past_participle = models.CharField(max_length=255, blank=True, null=True)
    explains = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'words'

    def __str__(self):
        s = self
        return str([
            s.spelling,
            s.phonetic,
            s.plurality,
            s.thirdpp,
            s.present_participle,
            s.past_tense,
            s.past_participle,
            s.explains
        ])


class Cet4WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'cet4_words_req'

    def __str__(self):
        s = self
        return str([s.wordorder, s.spelling])


class Cet6WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'cet6_words_req'

    def __str__(self):
        s = self
        return str([s.wordorder, s.spelling])


class NeepWordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        # managed=False
        db_table = 'neep_words_req'

    def __str__(self):
        s = self
        return str([s.wordorder, s.spelling])


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

