# Generated by Django 4.0.4 on 2022-05-22 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordnotes',
            old_name='uid',
            new_name='user',
        ),
    ]
