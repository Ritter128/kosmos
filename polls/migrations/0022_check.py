# Generated by Django 4.1.5 on 2023-03-30 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0021_alter_room_host'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reciever', models.CharField(default='Anon', max_length=20)),
                ('sender', models.CharField(default='Anon', max_length=20)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]
