# Generated by Django 3.2.5 on 2022-06-15 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0012_auto_20220615_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(choices=[('option_b', models.CharField(blank=True, max_length=50, null=True)), ('option_a', models.CharField(blank=True, max_length=50, null=True)), ('option_d', models.CharField(blank=True, max_length=50, null=True)), ('option_c', models.CharField(blank=True, max_length=50, null=True))], default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='question',
            name='cognitive_level',
            field=models.CharField(choices=[('Knowledge', 'Knowledge'), ('Application', 'Application'), ('Comprehension', 'Comprehension')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty_level',
            field=models.CharField(choices=[('Hard', 'Hard'), ('Medium', 'Medium'), ('Easy', 'Easy')], default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('Match_the_following', 'Match_the_following'), ('Fill_in_the_blanks', 'Fill_in_the_blanks'), ('MCQ', 'MCQ')], default='0', max_length=20),
        ),
    ]
