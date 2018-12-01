# Generated by Django 2.1.3 on 2018-11-30 23:25

from django.db import migrations, models
import redeneural.meetup_group.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetupGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(blank=True, null=True, upload_to=redeneural.meetup_group.models.get_meetup_group_image_path, verbose_name='Image')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to=redeneural.meetup_group.models.get_meetup_group_cover_path, verbose_name='Cover Image')),
            ],
            options={
                'verbose_name': 'Meetup Group',
                'verbose_name_plural': 'Meetup Groups',
            },
        ),
    ]
