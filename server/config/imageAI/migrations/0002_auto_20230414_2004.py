# Generated by Django 3.1.3 on 2023-04-14 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageAI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storyimage',
            name='image',
            field=models.TextField(max_length=500),
        ),
    ]
