# Generated by Django 4.2.7 on 2024-04-18 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidatemanagement', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='candidate',
            table='candidates',
        ),
        migrations.AlterModelTable(
            name='examcandidate',
            table='exam_candidates',
        ),
    ]