# Generated by Django 3.2 on 2023-01-26 12:02

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicians', '0003_auto_20230125_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='post_author',
            field=models.ForeignKey(default=django.contrib.auth.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author of post'),
        ),
    ]
