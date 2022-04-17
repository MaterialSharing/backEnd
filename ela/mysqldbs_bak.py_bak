# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlogAuthor(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=254)

    class Meta:
        managed = False
        db_table = 'blog_author'


class BlogBlog(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    class Meta:
        managed = False
        db_table = 'blog_blog'


class BlogEntry(models.Model):
    id = models.BigAutoField(primary_key=True)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    number_of_comments = models.IntegerField()
    number_of_pingbacks = models.IntegerField()
    rating = models.IntegerField()
    blog = models.ForeignKey(BlogBlog, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_entry'


class BlogEntryAuthors(models.Model):
    id = models.BigAutoField(primary_key=True)
    entry = models.ForeignKey(BlogEntry, models.DO_NOTHING)
    author = models.ForeignKey(BlogAuthor, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blog_entry_authors'
        unique_together = (('entry', 'author'),)


class Cet4WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cet4_words_req'


class Cet6WordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cet6_words_req'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ExamReq(models.Model):
    examtype = models.CharField(db_column='examType', primary_key=True, max_length=1)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'exam_req'


class FeedBack(models.Model):
    uid = models.IntegerField(primary_key=True)
    content = models.CharField(max_length=255)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'feed_back'


class LongSentences(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    contenten = models.CharField(db_column='contentEN', max_length=255)  # Field name made lowercase.
    explaincn = models.CharField(db_column='explainCN', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'long_sentences'


class NeepWordsReq(models.Model):
    wordorder = models.AutoField(db_column='wordOrder', primary_key=True)  # Field name made lowercase.
    spelling = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'neep_words_req'


class PollsChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    test = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'polls_question'


class ScoreImproverNeepStudy(models.Model):
    sid = models.IntegerField(db_column='SID', primary_key=True)  # Field name made lowercase.
    wid = models.CharField(max_length=255)
    last_see_datetime = models.DateTimeField(blank=True, null=True)
    familiarity = models.IntegerField()
    study_progress = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'score_improver_neep_study'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    signin = models.IntegerField(db_column='signIn')  # Field name made lowercase.
    examtype = models.CharField(db_column='examType', max_length=1)  # Field name made lowercase.
    examdate = models.DateField(db_column='examDate')  # Field name made lowercase.
    signupdate = models.DateField(db_column='signUpDate')  # Field name made lowercase.
    test = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class WordNotes(models.Model):
    id = models.BigAutoField(primary_key=True)
    wordspelling = models.CharField(db_column='wordSpelling', max_length=255, blank=True, null=True)  # Field name made lowercase.
    uid = models.IntegerField(db_column='UID', blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(max_length=255, blank=True, null=True)
    difficulty_rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'word_notes'


class WordSearchHistory(models.Model):
    uid = models.IntegerField(primary_key=True)
    spelling = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'word_search_history'
        unique_together = (('uid', 'spelling'),)


class WordStar(models.Model):
    uid = models.IntegerField(primary_key=True)
    spelling = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'word_star'
        unique_together = (('uid', 'spelling'),)


class Words(models.Model):
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
        managed = False
        db_table = 'words'
