# Generated by Django 4.2.6 on 2024-03-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidatemanagement', '0001_initial'),
        ('exam_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='examcandidate',
            name='exam_subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.examsubjects'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidates', to='exam_management.exam'),
        ),
    ]