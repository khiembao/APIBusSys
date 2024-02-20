# Generated by Django 4.2.8 on 2024-02-19 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sysman', '0003_trippath'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('active', models.BooleanField(default=True)),
                ('bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sysman.bus')),
            ],
        ),
    ]
