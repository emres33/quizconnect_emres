# Generated by Django 5.0 on 2023-12-19 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_question_question_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='lesson',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app.lesson'),
        ),
    ]