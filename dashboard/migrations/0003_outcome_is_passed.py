# Generated by Django 5.0.3 on 2024-03-17 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_alter_outcome_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='outcome',
            name='is_passed',
            field=models.BooleanField(default=True),
        ),
    ]
