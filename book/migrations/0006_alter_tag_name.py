# Generated by Django 5.2.3 on 2025-07-20 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0005_tag_create_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tag",
            name="name",
            field=models.CharField(db_column="tag_name", max_length=100, unique=True),
        ),
    ]
