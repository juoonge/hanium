# Generated by Django 4.2.1 on 2023-05-17 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fairytale', '0009_alter_story_id_alter_storyelement_element_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storyelement',
            old_name='story_name',
            new_name='story_id',
        ),
        migrations.AlterField(
            model_name='story',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]
