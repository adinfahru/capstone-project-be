# Generated by Django 5.1.3 on 2024-12-11 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quizsession',
            options={'ordering': ['order']},
        ),
    ]
