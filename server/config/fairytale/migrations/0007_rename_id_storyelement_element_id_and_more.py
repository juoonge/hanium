# Generated by Django 4.2.1 on 2023-05-17 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fairytale', '0006_alter_story_author_alter_story_title_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyelement',
            old_name='id',
            new_name='element_id',
        ),
        migrations.RenameField(
            model_name='storyelement',
            old_name='story_id',
            new_name='story_name',
        ),
    ]