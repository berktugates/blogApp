# Generated by Django 4.2.4 on 2023-08-19 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_topweek_last_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='topweek',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
