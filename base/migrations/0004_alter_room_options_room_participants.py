# Generated by Django 5.0.4 on 2024-09-15 02:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_room_host"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-updated", "-created"]},
        ),
        migrations.AddField(
            model_name="room",
            name="participants",
            field=models.ManyToManyField(
                blank=True, related_name="participants", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
