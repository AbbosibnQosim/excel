# Generated by Django 3.1.5 on 2021-01-19 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0009_object_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websites',
            name='description',
        ),
        migrations.RemoveField(
            model_name='websites',
            name='resultfile',
        ),
        migrations.AddField(
            model_name='websites',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', tinymce.models.HTMLField(blank=True)),
                ('resultfile', models.FileField(upload_to='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
