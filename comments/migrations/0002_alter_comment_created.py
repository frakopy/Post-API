# Generated by Django 4.2.1 on 2023-06-22 17:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
