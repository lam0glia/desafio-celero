# Generated by Django 3.1.4 on 2020-12-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_olympic_history', '0007_auto_20201210_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
