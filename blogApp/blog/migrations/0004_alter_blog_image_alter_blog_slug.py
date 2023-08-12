# Generated by Django 4.2.4 on 2023-08-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(editable=False, unique=True),
        ),
    ]
