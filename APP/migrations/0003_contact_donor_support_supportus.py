# Generated by Django 3.1.1 on 2021-03-05 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0002_auto_20201231_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('contactnum', models.CharField(max_length=30)),
                ('messege', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_no', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('messege', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Supportus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('drive_date', models.CharField(max_length=30)),
                ('messege', models.CharField(max_length=150)),
            ],
        ),
    ]
