# Generated by Django 4.1.3 on 2022-11-04 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicplaylist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
