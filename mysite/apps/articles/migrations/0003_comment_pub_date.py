# Generated by Django 3.1 on 2020-08-26 21:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200826_1951'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 26, 21, 23, 24, 757660, tzinfo=utc), verbose_name='дата публикации'),
        ),
    ]