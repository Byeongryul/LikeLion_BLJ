# Generated by Django 2.1.7 on 2019-08-09 13:55

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('Designfeed', '0002_designfeed_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(allow_unicode=True, max_length=100, unique=True, verbose_name='slug')),
            ],
            options={
                'verbose_name': 'tag',
                'verbose_name_plural': 'tags',
            },
        ),
        migrations.CreateModel(
            name='TaggedPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Designfeed.DesignFeed')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designfeed_taggedpost_items', to='Designfeed.PostTag')),
            ],
            options={
                'verbose_name': 'tagged post',
                'verbose_name_plural': 'tagged posts',
            },
        ),
        migrations.AddField(
            model_name='designfeed',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='Designfeed.TaggedPost', to='Designfeed.PostTag', verbose_name='tags'),
        ),
    ]
