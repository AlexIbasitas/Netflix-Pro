# Generated by Django 4.0.3 on 2024-04-30 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_co2'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetflixMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField()),
                ('duration', models.DurationField()),
                ('attributes', models.TextField()),
                ('title', models.CharField(max_length=255)),
                ('supplemental_video_type', models.CharField(max_length=100)),
                ('device_type', models.CharField(max_length=100)),
                ('bookmark', models.DurationField()),
                ('latest_bookmark', models.DurationField()),
                ('country', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('start_time',),
            },
        ),
    ]