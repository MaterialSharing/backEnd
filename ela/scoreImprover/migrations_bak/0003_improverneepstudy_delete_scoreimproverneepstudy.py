# Generated by Django 4.0.3 on 2022-05-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoreImprover', '0002_delete_cet4wordsreq_delete_cet6wordsreq_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImproverNeepStudy',
            fields=[
                ('id', models.IntegerField(db_column='SID', primary_key=True, serialize=False)),
                ('wid', models.IntegerField(default=0)),
                ('last_see_datetime', models.DateTimeField(blank=True, null=True)),
                ('familiarity', models.IntegerField(default=0, help_text='熟练度')),
                ('study_progress', models.IntegerField()),
            ],
            options={
                'db_table': 'neep_study',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='ScoreImproverNeepStudy',
        ),
    ]