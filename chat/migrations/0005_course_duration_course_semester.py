# Generated by Django 4.2.1 on 2023-05-12 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='duration',
            field=models.CharField(default='Unknown', max_length=50),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.IntegerField(default=0),
        ),
    ]
