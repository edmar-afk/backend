# Generated by Django 5.0.3 on 2024-04-06 10:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_buttonclick_visit_alter_comments_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 10, 3, 14, 662421, tzinfo=datetime.timezone.utc)),
        ),
    ]