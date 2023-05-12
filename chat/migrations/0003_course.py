# Generated by Django 4.2.1 on 2023-05-12 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='course_images/')),
                ('description', models.TextField()),
                ('mission', models.TextField()),
                ('vision', models.TextField()),
                ('peo', models.TextField()),
                ('po', models.TextField()),
                ('pso', models.TextField()),
            ],
        ),
    ]