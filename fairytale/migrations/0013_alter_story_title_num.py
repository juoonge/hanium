# Generated by Django 4.2.1 on 2023-06-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fairytale", "0012_story_title_num"),
    ]

    operations = [
        migrations.AlterField(
            model_name="story",
            name="title_num",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
