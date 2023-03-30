# Generated by Django 4.1.5 on 2023-02-15 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0017_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No name', max_length=20)),
                ('desc', models.TextField(verbose_name='blank')),
                ('content', models.TextField(verbose_name='blank')),
            ],
        ),
    ]