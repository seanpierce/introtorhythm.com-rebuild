# Generated by Django 2.2.4 on 2019-09-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribers', '0002_auto_20190811_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscriptionrequest',
            name='ip_address',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
