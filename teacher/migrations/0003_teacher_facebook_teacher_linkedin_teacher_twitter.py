# Generated by Django 5.0.3 on 2024-04-17 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
