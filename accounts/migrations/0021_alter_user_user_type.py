# Generated by Django 3.2.5 on 2022-06-15 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_user_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(blank=True, choices=[('is_student', 'is_student'), ('is_admin', 'is_admin'), ('is_staff', 'is_staff'), ('-------', '-------')], default='0', max_length=20, null=True),
        ),
    ]
