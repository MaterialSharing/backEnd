# Generated by Django 4.0.3 on 2022-05-08 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_wordsearchhistory_spelling_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestForeignKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.CharField(max_length=50)),
                ('user', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_testF', to='user.user')),
            ],
        ),
    ]
