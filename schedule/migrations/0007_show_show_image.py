# Generated by Django 3.1.14 on 2022-10-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0006_auto_20220301_0939'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='show_image',
            field=models.ImageField(blank=True, max_length=500, upload_to='shows/images/'),
        ),
    ]
