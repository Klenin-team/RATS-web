# Generated by Django 5.0 on 2024-01-02 04:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("problems", "0004_alter_problems_id_alter_solves_id_alter_tests_id_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Solves",
            new_name="Solutions",
        ),
    ]
