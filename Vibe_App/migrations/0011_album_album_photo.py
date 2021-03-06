# Generated by Django 2.2 on 2022-02-25 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vibe_App', '0010_auto_20220224_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Album_Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('cover', models.ImageField(blank=True, default='deafault.png', upload_to='')),
                ('album_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album_image', to='Vibe_App.Album')),
            ],
        ),
    ]
