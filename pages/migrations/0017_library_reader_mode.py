# Generated by Django 2.1.2 on 2018-10-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_auto_20180925_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='reader_mode',
            field=models.PositiveSmallIntegerField(choices=[(0, 'default'), (1, 'dark'), (2, 'light')], default=0),
        ),
    ]
