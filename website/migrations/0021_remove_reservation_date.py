# Generated by Django 4.0.6 on 2023-01-22 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_reservation_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='date',
        ),
    ]