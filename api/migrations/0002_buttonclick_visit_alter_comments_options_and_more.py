# Generated by Django 5.0.3 on 2024-04-06 10:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ButtonClick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_identifier', models.CharField(max_length=100, unique=True)),
                ('visit_count', models.IntegerField(default=0)),
                ('visited_today', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='products',
            options={'verbose_name': 'Product'},
        ),
        migrations.AlterField(
            model_name='comments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 4, 6, 10, 2, 1, 27558, tzinfo=datetime.timezone.utc)),
        ),
    ]