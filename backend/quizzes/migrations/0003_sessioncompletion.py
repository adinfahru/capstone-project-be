# Generated by Django 5.1.3 on 2024-12-14 03:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_alter_quizsession_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed_at', models.DateTimeField(auto_now_add=True)),
                ('attempt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_completions', to='quizzes.quizattempt')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='completions', to='quizzes.quizsession')),
            ],
            options={
                'unique_together': {('attempt', 'session')},
            },
        ),
    ]