# Generated by Django 4.0.1 on 2022-01-05 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_model_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date',
        ),
    ]
