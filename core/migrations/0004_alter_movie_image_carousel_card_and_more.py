# Generated by Django 5.0.4 on 2024-04-06 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_movie_playback_movie_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_carousel_card',
            field=models.ImageField(default='images/default_image.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_feature_cover',
            field=models.FileField(default='images/default_image.png', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='video',
            field=models.FileField(default='images/default_image.png', upload_to='movie/'),
        ),
    ]