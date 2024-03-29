# Generated by Django 4.2.8 on 2024-02-19 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sysman', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('model', models.CharField(max_length=50)),
                ('bienso', models.CharField(max_length=100)),
                ('capacity', models.IntegerField(default=45)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SpecialOccasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_date', models.DateTimeField(auto_now=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='destination',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='destination',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
