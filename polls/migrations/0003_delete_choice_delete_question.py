# Generated by Django 4.1.5 on 2023-01-26 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]