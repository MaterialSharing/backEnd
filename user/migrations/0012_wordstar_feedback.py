# Generated by Django 4.0.3 on 2022-05-08 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_delete_feedback_delete_wordstar'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordStar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spelling', models.IntegerField()),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_word_star', to='user.user')),
            ],
            options={
                'db_table': 'word_star',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_feedback', to='user.user')),
            ],
            options={
                'db_table': 'feed_back',
                'managed': True,
            },
        ),
    ]
