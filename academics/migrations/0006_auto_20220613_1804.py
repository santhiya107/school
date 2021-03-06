# Generated by Django 3.2.5 on 2022-06-13 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_auto_20220613_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='difficulty_level',
            field=models.CharField(choices=[('Medium', 'Medium'), ('Hard', 'Hard'), ('Easy', 'Easy')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='cognitive_level',
            field=models.CharField(choices=[('Knowledge', 'Knowledge'), ('Application', 'Application'), ('Comprehension', 'Comprehension')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('MCQ', 'MCQ'), ('Match_the_following', 'Match_the_following'), ('Fill_in_the_blanks', 'Fill_in_the_blanks')], default='0', max_length=20),
        ),
    ]
