# Generated by Django 4.1.5 on 2023-01-26 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_delete_choice_delete_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='person_age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='person_name',
            new_name='name',
        ),
    ]