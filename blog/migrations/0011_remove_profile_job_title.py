# Generated by Django 4.2.3 on 2023-07-10 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_comment_song_alter_profile_user_delete_social_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='job_title',
        ),
    ]
