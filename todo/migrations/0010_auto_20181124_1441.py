# Generated by Django 2.1.3 on 2018-11-24 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20181124_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='is_done',
            field=models.BooleanField(default=False, verbose_name='Сделано'),
        ),
    ]
