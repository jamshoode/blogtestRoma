# Generated by Django 3.1 on 2020-08-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default="Shoode's BLOG", max_length=255),
        ),
    ]
