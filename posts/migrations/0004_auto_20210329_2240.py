# Generated by Django 2.1.7 on 2021-03-29 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210329_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 29, 22, 40, 50, 534293)),
        ),
    ]