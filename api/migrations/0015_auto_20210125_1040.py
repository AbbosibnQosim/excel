# Generated by Django 3.1.5 on 2021-01-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20210121_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='object',
            name='name',
            field=models.TextField(verbose_name='Объект номи'),
        ),
    ]
