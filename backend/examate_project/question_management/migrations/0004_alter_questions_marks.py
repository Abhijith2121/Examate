# Generated by Django 4.2.7 on 2024-03-18 09:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question_management', '0003_alter_questions_question_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='marks',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
