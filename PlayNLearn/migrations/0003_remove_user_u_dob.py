# Generated by Django 2.0.4 on 2018-05-17 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PlayNLearn', '0002_auto_20180501_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='U_DOB',
        ),
    ]
