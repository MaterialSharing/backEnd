# Generated by Django 4.0.3 on 2022-04-17 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='examdate',
            field=models.DateField(db_column='examDate', default='1970-01-01'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(default='name_id', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='signin',
            field=models.IntegerField(db_column='signIn', default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='signupdate',
            field=models.DateField(db_column='signUpDate', default='1970-01-01'),
        ),
    ]
