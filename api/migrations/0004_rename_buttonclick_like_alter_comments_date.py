# Generated by Django 5.0.3 on 2024-04-06 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_comments_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ButtonClick',
            new_name='Like',
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 10, 6, 21, 269482, tzinfo=datetime.timezone.utc)),
        ),
    ]