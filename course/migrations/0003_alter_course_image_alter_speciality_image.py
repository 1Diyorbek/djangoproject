# Generated by Django 5.0.3 on 2024-04-17 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_course_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='course'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='image',
            field=models.ImageField(upload_to='speciality'),
        ),
    ]