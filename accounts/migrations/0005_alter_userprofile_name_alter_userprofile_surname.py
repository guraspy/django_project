# Generated by Django 5.0.2 on 2024-03-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_name_userprofile_profileimg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='surname',
            field=models.TextField(blank=True, null=True),
        ),
    ]
