# Generated by Django 4.0.4 on 2022-05-31 03:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_topic_category_alter_student_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2022, 5, 31, 3, 40, 18, 883303, tzinfo=utc)),
        ),
    ]