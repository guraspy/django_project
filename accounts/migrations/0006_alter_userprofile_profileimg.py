# Generated by Django 5.0.2 on 2024-03-04 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_name_alter_userprofile_surname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profileimg',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images/'),
        ),
    ]