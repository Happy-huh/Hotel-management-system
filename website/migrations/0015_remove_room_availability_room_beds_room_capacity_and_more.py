# Generated by Django 4.0.6 on 2023-01-05 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_reservation_check_in_reservation_check_out'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='availability',
        ),
        migrations.AddField(
            model_name='room',
            name='beds',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Roomtac',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.room')),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='roomtac',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='website.roomtac'),
        ),
    ]
