# Generated by Django 3.1.1 on 2024-07-08 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_auto_20240706_1630"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                (
                    "posts",
                    models.ManyToManyField(
                        blank=True, related_name="categories", to="blogging.Post"
                    ),
                ),
            ],
        ),
    ]
