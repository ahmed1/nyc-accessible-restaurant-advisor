# Generated by Django 3.1.2 on 2020-10-28 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accessible_restaurant', '0007_auto_20201027_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='img_url',
            field=models.URLField(blank=True, default='https://i.pinimg.com/originals/4e/24/f5/4e24f523182e09376bfe8424d556610a.png', max_length=250),
        ),
    ]
