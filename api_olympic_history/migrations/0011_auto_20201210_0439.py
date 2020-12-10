# Generated by Django 3.1.4 on 2020-12-10 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_olympic_history', '0010_auto_20201210_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='height',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='weight',
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='athlete_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='athlete_height',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='athleteevent',
            name='athlete_weight',
            field=models.FloatField(null=True),
        ),
    ]
