# Generated by Django 3.1.4 on 2020-12-09 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_olympic_history', '0003_medal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=1)),
                ('height', models.CharField(max_length=3)),
                ('weight', models.CharField(max_length=3)),
            ],
        ),
    ]
