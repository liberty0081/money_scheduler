# Generated by Django 5.0.3 on 2024-03-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_merge_0004_alter_outcome_date_0004_alter_outcome_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outcome',
            name='is_passed',
            field=models.BooleanField(default=False),
        ),
    ]