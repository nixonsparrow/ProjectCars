# Generated by Django 4.0 on 2021-12-25 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_rate_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='avg_rating',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
