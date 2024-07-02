# Generated by Django 4.2.6 on 2024-03-05 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('subject_management', '0001_initial'),
        ('candidatemanagement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('exam_duration', models.IntegerField(null=True)),
                ('scheduled_time', models.DateTimeField()),
                ('status', models.SmallIntegerField(choices=[(0, 'created'), (1, 'completed'), (2, 'evaluated'), (3, 'result_published')], default=0)),
                ('candidate_count', models.IntegerField(default=0)),
                ('access_link', models.CharField(blank=True, max_length=255)),
                ('instructions', models.CharField(blank=True, max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(blank=True, max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidatemanagement.candidate')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.exam')),
            ],
        ),
        migrations.CreateModel(
            name='ExamSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_duration', models.IntegerField()),
                ('pass_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('difficulty_level', models.PositiveSmallIntegerField(choices=[(1, 'easy'), (2, 'medium'), (3, 'difficult')])),
                ('question_count', models.IntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exam_subjects', to='exam_management.exam')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject_management.subject')),
            ],
        ),
        migrations.CreateModel(
            name='ExamQuestions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam_management.examsubjects')),
            ],
        ),
    ]
