# Generated by Django 4.0.4 on 2022-05-26 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_user_password_hash_user_password_salt'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.IntegerField(default=0, help_text="User's status(admin or normal user,even the disabled or deleted user(not real delete,just modify the status.)"),
        ),
    ]
