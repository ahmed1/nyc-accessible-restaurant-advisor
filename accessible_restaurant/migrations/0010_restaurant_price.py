# Generated by Django 3.1.2 on 2020-10-31 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accessible_restaurant", "0009_auto_20201028_1114"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="price",
            field=models.CharField(blank=True, max_length=5),
        ),
    ]