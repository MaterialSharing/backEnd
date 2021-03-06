# Generated by Django 4.0.4 on 2022-05-15 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0005_wordmatcher'),
        ('user', '0018_user_openid'),
        ('scoreImprover', '0010_rename_uid_neepstudy_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cet4study',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cet6study',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='user.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cet4study',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cet4study',
            name='last_see_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='cet4study',
            name='wid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='word.neepwordsreq'),
        ),
        migrations.AlterField(
            model_name='cet6study',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cet6study',
            name='last_see_datetime',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='cet6study',
            name='wid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='word.neepwordsreq'),
        ),
    ]
