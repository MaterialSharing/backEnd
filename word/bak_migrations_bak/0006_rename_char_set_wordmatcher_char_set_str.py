# Generated by Django 4.0.4 on 2022-05-17 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_wordmatcher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wordmatcher',
            old_name='char_set',
            new_name='char_set_str',
        ),
    ]