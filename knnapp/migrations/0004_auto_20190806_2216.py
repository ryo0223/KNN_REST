# Generated by Django 2.2.2 on 2019-08-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knnapp', '0003_auto_20190803_1214'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='ssid',
        ),
        migrations.AlterField(
            model_name='file',
            name='student_id',
            field=models.CharField(max_length=15),
        ),
    ]
