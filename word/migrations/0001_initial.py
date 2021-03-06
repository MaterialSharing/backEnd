# Generated by Django 4.0.4 on 2022-05-19 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cet4WordsReq',
            fields=[
                ('wordorder', models.AutoField(db_column='wordOrder', primary_key=True, serialize=False)),
                ('spelling', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cet4_words_req',
            },
        ),
        migrations.CreateModel(
            name='Cet6WordsReq',
            fields=[
                ('wordorder', models.AutoField(db_column='wordOrder', primary_key=True, serialize=False)),
                ('spelling', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'cet6_words_req',
            },
        ),
        migrations.CreateModel(
            name='NeepWordsReq',
            fields=[
                ('wordorder', models.AutoField(db_column='wordOrder', primary_key=True, serialize=False)),
                ('spelling', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'neep_words_req',
            },
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('wid', models.AutoField(primary_key=True, serialize=False)),
                ('spelling', models.CharField(max_length=255)),
                ('phonetic', models.CharField(blank=True, max_length=255, null=True)),
                ('plurality', models.CharField(blank=True, help_text='noun plural', max_length=255, null=True)),
                ('thirdpp', models.CharField(blank=True, help_text='3rd person present', max_length=255, null=True)),
                ('present_participle', models.CharField(blank=True, max_length=255, null=True)),
                ('past_tense', models.CharField(blank=True, max_length=255, null=True)),
                ('past_participle', models.CharField(blank=True, max_length=255, null=True)),
                ('explains', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'words',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='WordMatcher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.CharField(max_length=255)),
                ('char_set_str', models.CharField(max_length=26)),
            ],
        ),
        migrations.CreateModel(
            name='WordNotes',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('uid', models.IntegerField(blank=True, db_column='UID', null=True)),
                ('spelling', models.CharField(blank=True, db_column='spelling', max_length=255, null=True)),
                ('content', models.CharField(blank=True, max_length=255, null=True)),
                ('difficulty_rate', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'word_notes',
                'managed': True,
            },
        ),
    ]
