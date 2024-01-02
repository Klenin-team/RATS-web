# Generated by Django 5.0 on 2024-01-02 03:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "problems",
            "0003_problems_memory_limitation_problems_time_limitation_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="problems",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="solves",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="tests",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
        migrations.AlterField(
            model_name="testverdicts",
            name="id",
            field=models.UUIDField(
                default=uuid.uuid4, editable=False, primary_key=True, serialize=False
            ),
        ),
    ]