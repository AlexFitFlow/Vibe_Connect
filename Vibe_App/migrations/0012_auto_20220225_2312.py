# Generated by Django 2.2 on 2022-02-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vibe_App', '0011_album_album_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album_photo',
            name='description',
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='album_photo',
            name='title',
            field=models.TextField(max_length=255, null=True),
        ),
    ]
