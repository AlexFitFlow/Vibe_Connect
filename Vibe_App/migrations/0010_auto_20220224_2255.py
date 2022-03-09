# Generated by Django 2.2 on 2022-02-24 22:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Vibe_App', '0009_auto_20220219_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_comment',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image_user_likes',
            field=models.ManyToManyField(related_name='image_liked_posts', to='Vibe_App.User'),
        ),
    ]