# Generated by Django 2.1.3 on 2018-11-24 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20181124_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_done',
        ),
    ]
