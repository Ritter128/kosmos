# Generated by Django 4.1.5 on 2023-02-17 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0018_room'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(default='No name', max_length=100),
        ),
    ]
