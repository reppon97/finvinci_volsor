# Generated by Django 4.0.1 on 2022-01-09 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairing',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
