# Generated by Django 3.2.9 on 2024-01-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_answer_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_image',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]