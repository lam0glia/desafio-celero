# Generated by Django 3.1.4 on 2020-12-10 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_olympic_history', '0006_auto_20201209_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='note',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]