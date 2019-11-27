# Generated by Django 2.2.4 on 2019-11-27 04:40

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('episodes', '0003_auto_20191127_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='episode',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
