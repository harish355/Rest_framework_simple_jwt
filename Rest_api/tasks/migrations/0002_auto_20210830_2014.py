# Generated by Django 3.2.5 on 2021-08-30 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tasks',
        ),
        migrations.DeleteModel(
            name='Tile',
        ),
    ]
