# Generated by Django 4.0.1 on 2022-01-05 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_student_address_alter_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
