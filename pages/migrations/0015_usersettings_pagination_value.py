# Generated by Django 2.1 on 2018-08-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0014_auto_20180809_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='pagination_value',
            field=models.PositiveSmallIntegerField(default=100),
        ),
    ]
