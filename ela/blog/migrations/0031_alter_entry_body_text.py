# Generated by Django 4.0.3 on 2022-04-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0030_alter_entry_body_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body_text',
            field=models.TextField(default='blogRand 33 body contents!'),
        ),
    ]
