# Generated by Django 4.0.6 on 2022-11-08 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_remove_category_post_room_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='category',
        ),
    ]