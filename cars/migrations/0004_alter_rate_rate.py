# Generated by Django 4.0 on 2021-12-23 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_alter_rate_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='rate',
            field=models.IntegerField(choices=[(1, 'Meh'), (2, 'Nothing special'), (3, 'Pretty OK'), (4, 'Likeable'), (5, 'Extraordinary!')], validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
