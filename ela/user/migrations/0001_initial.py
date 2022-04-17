# Generated by Django 4.0.3 on 2022-04-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
            ],
            options={
                'db_table': 'feed_back',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('signin', models.IntegerField(db_column='signIn')),
                ('examtype', models.CharField(db_column='examType', max_length=1)),
                ('examdate', models.DateField(db_column='examDate')),
                ('signupdate', models.DateField(db_column='signUpDate')),
                ('test', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='name_id', max_length=20)),
                ('signin', models.IntegerField(db_column='signIn', default=0)),
                ('examtype', models.CharField(db_column='examType', max_length=1)),
                ('examdate', models.DateField(db_column='examDate', default='1970-01-01')),
                ('signupdate', models.DateField(db_column='signUpDate', default='1970-01-01')),
            ],
            options={
                'db_table': 'user_info',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WordStar',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('spelling', models.IntegerField()),
            ],
            options={
                'db_table': 'word_star',
                'managed': True,
                'unique_together': {('uid', 'spelling')},
            },
        ),
        migrations.CreateModel(
            name='WordSearchHistory',
            fields=[
                ('uid', models.IntegerField(primary_key=True, serialize=False)),
                ('spelling', models.IntegerField()),
            ],
            options={
                'db_table': 'word_search_history',
                'managed': True,
                'unique_together': {('uid', 'spelling')},
            },
        ),
    ]
