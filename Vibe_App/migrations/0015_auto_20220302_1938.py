# Generated by Django 2.2 on 2022-03-02 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vibe_App', '0014_album_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_comment',
        ),
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('image_message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_comments', to='Vibe_App.Post')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_comments', to='Vibe_App.User')),
            ],
        ),
    ]
