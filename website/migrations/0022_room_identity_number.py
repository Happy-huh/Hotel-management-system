# Generated by Django 4.0.6 on 2023-01-24 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_remove_reservation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='identity_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
