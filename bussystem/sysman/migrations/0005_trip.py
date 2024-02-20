# Generated by Django 4.2.8 on 2024-02-19 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sysman', '0004_seat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_depart_time', models.DateTimeField(blank=True, null=True)),
                ('trip_arrive_time', models.DateTimeField(blank=True, null=True)),
                ('bus', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sysman.bus')),
                ('trip_path', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sysman.trippath')),
            ],
        ),
    ]
