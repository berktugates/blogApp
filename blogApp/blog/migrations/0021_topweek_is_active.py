# Generated by Django 4.2.4 on 2023-08-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_topweek_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='topweek',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
