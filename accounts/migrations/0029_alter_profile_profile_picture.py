# Generated by Django 3.2.5 on 2022-06-24 07:02

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, default='user_profile/profile.png', null=True, upload_to=accounts.models.Profile.upload_design_to),
        ),
    ]
