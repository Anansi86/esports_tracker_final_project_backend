# Generated by Django 4.1.3 on 2022-11-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('esports_app', '0004_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='teams',
            field=models.ManyToManyField(related_name='players', to='esports_app.team'),
        ),
    ]
