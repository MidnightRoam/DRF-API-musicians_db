# Generated by Django 3.2 on 2023-01-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='musician',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
