# Generated by Django 4.2.2 on 2025-04-21 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0007_comments_post"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="login_require",
            field=models.BooleanField(default=False),
        ),
    ]
