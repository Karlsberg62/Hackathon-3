# Generated by Django 4.2.11 on 2024-03-07 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon3', '0002_post_excerpt_alter_post_date_alter_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
