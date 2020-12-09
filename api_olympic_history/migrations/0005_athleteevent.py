# Generated by Django 3.1.4 on 2020-12-09 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api_olympic_history', '0004_athlete'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('athlete', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_olympic_history.athlete')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_olympic_history.event')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_olympic_history.game')),
                ('medal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_olympic_history.medal')),
            ],
        ),
    ]