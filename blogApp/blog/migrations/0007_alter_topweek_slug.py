# Generated by Django 4.2.4 on 2023-08-11 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_topweek'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topweek',
            name='slug',
            field=models.SlugField(editable=False, null=True, unique=True),
        ),
    ]
