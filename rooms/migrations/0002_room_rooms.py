# Generated by Django 4.1.6 on 2023-03-06 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rooms", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="room",
            name="rooms",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
