# Generated by Django 2.2.4 on 2019-11-27 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('episodes', '0005_auto_20191127_0441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='episode',
            old_name='genres',
            new_name='tags',
        ),
    ]
