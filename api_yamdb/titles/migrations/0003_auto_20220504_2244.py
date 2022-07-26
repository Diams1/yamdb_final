# Generated by Django 2.2.16 on 2022-05-04 19:44

import titles.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0002_auto_20220504_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.IntegerField(db_index=True, validators=[titles.validators.validate_year], verbose_name='Год выпуска'),
        ),
    ]
