# Generated by Django 4.1.5 on 2023-02-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_person_wealth'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='ethnicity',
            field=models.CharField(default='Not specified', max_length=20),
        ),
    ]