# Generated by Django 5.0.2 on 2024-03-31 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_likepost_tweet_no_of_likes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likepost',
            old_name='post_id',
            new_name='tweet_id',
        ),
    ]
