# Generated by Django 4.0.4 on 2022-05-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_alter_user_signupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='openid',
            field=models.CharField(default=None, max_length=150, null=True, unique=True),
        ),
    ]