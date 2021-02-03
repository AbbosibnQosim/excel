# Generated by Django 3.1.5 on 2021-01-19 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0010_auto_20210119_1311'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Websites',
            new_name='Website',
        ),
        migrations.AddField(
            model_name='result',
            name='website',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.website'),
            preserve_default=False,
        ),
    ]