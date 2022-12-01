# Generated by Django 4.1.3 on 2022-11-29 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0003_team_match_team1_match_team2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=25, unique=True)),
                ('alias_name', models.CharField(max_length=25, unique=True)),
                ('player_num', models.IntegerField()),
                ('hometown', models.CharField(max_length=25, unique=True)),
                ('pic', models.URLField()),
            ],
        ),
    ]
