# Generated by Django 2.2.3 on 2019-07-10 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthapp', '0003_schedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='end_time',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='schedule',
            name='start_time',
            field=models.CharField(default='', max_length=30),
        ),
    ]
