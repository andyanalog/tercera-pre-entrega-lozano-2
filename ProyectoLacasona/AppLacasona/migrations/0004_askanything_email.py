# Generated by Django 4.2.5 on 2023-09-29 03:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AppLacasona", "0003_remove_sendsong_deadline_sendsong_email_sendsong_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="askanything",
            name="email",
            field=models.EmailField(default="correo@ejemplo.com", max_length=254),
        ),
    ]
