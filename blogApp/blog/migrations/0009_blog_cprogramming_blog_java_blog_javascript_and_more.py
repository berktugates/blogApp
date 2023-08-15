# Generated by Django 4.2.4 on 2023-08-12 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_blog_author_alter_blog_slug_alter_topweek_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='CProgramming',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='java',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='javascript',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='python',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]
