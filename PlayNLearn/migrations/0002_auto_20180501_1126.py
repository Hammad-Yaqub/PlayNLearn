# Generated by Django 2.0.4 on 2018-05-01 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PlayNLearn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='user',
            name='U_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
