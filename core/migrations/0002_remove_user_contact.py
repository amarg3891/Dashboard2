# Generated by Django 3.1.2 on 2021-01-11 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact',
        ),
    ]