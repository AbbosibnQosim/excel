# Generated by Django 3.1.5 on 2021-01-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210119_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='phone',
            field=models.TextField(blank=True),
        ),
    ]
