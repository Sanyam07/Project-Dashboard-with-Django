# Generated by Django 2.1.7 on 2019-03-16 21:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190316_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='cost',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=3, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='project',
            name='budget',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=6, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requiredskills',
            name='css',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requiredskills',
            name='db',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requiredskills',
            name='html',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requiredskills',
            name='js',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='requiredskills',
            name='python',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=1, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]