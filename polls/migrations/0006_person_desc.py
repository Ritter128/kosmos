# Generated by Django 4.1.5 on 2023-01-26 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_person_accdate_alter_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='desc',
            field=models.TextField(default='empty'),
        ),
    ]
