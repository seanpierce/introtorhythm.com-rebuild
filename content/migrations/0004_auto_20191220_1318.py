# Generated by Django 2.2.4 on 2019-12-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_auto_20191220_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(default='img-12202019-13:18:46', max_length=50),
        ),
    ]
