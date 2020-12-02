# Generated by Django 3.1.2 on 2020-12-02 05:51

import accessible_restaurant.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accessible_restaurant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=128)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='restaurant',
            name='cuisine',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='main_category1',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='main_category2',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='main_category3',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='review_count',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='user_profile',
            name='borough',
            field=models.CharField(choices=[('Manhattan', 'Manhattan'), ('Brooklyn', 'Brooklyn'), ('Queens', 'Queens'), ('The Bronx', 'The Bronx'), ('Staten Island', 'Staten Island'), ('Not Applicable', 'Not Applicable')], default='None Selected', max_length=128),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='phone',
            field=models.PositiveSmallIntegerField(blank=True, default=1234567889, validators=[accessible_restaurant.models.User_Profile.validate_phone]),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='state',
            field=models.CharField(choices=[('Alabama', 'Alabama'), ('Alaska', 'Alaska'), ('Arizona', 'Arizona'), ('Arkansas', 'Arkansas'), ('California', 'California'), ('Colorado', 'Colorado'), ('Connecticut', 'Connecticut'), ('Delaware', 'Delaware'), ('District of Columbia', 'District of Columbia'), ('Florida', 'Florida'), ('Georgia', 'Georgia'), ('Hawaii', 'Hawaii'), ('Idaho', 'Idaho'), ('Illinois', 'Illinois'), ('Indiana', 'Indiana'), ('Iowa', 'Iowa'), ('Kansas', 'Kansas'), ('Kentucky', 'Kentucky'), ('Louisiana', 'Louisiana'), ('Maine', 'Maine'), ('Montana', 'Montana'), ('Nebraska', 'Nebraska'), ('Nevada', 'Nevada'), ('New Hampshire', 'New Hampshire'), ('New Jersey', 'New Jersey'), ('New Mexico', 'New Mexico'), ('New York', 'New York'), ('North Carolina', 'North Carolina'), ('North Dakota', 'North Dakota'), ('Ohio', 'Ohio'), ('Oklahoma', 'Oklahoma'), ('Oregon', 'Oregon'), ('Maryland', 'Maryland'), ('Massachusetts', 'Massachusetts'), ('Michigan', 'Michigan'), ('Minnesota', 'Minnesota'), ('Mississippi', 'Mississippi'), ('Missouri', 'Missouri'), ('Pennsylvania', 'Pennsylvania'), ('Rhode Island', 'Rhode Island'), ('South Carolina', 'South Carolina'), ('South Dakota', 'South Dakota'), ('Tennessee', 'Tennessee'), ('Texas', 'Texas'), ('Utah', 'Utah'), ('Vermont', 'Vermont'), ('Virginia', 'Virginia'), ('Washington', 'Washington'), ('West Virginia', 'West Virginia'), ('Wisconsin', 'Wisconsin'), ('Wyoming', 'Wyoming')], default='None Selected', max_length=128),
        ),
        migrations.AlterField(
            model_name='user_profile',
            name='zip_code',
            field=models.PositiveSmallIntegerField(blank=True, default=12345, validators=[accessible_restaurant.models.User_Profile.validate_zip]),
        ),
        migrations.CreateModel(
            name='User_Preferences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dining_pref1', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dining_pref2', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dining_pref3', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Non-Alcoholic Drinks', 'Non-Alcoholic Drinks'), ('Alcoholic Drinks', 'Alcoholic Drinks'), ('Dessert', 'Dessert'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('budget_pref', models.CharField(choices=[('$', '$'), ('$$', '$$'), ('$$$', '$$$'), ('$$$$', '$$$$'), ('No Preference', 'No Preference')], default='No Preference', max_length=15)),
                ('location_pref', models.CharField(choices=[('Near Home', 'Near Home'), ('Within My Borough', 'Within My Borough'), ('Outside My Borough', 'Outside My Borough'), ('No Preference', 'No Preference')], default='No Preference', max_length=20)),
                ('dietary_pref', models.CharField(choices=[('Vegetarian', 'Vegetarian'), ('Gluten-Free', 'Gluten-Free'), ('Salads Available', 'Salads Available'), ('None', 'None')], default='None', max_length=20)),
                ('cuisine_pref1', models.CharField(choices=[('Asian', 'Asian'), ('American', 'American'), ('Caribbean', 'Caribbean'), ('European', 'European'), ('Indian', 'Indian'), ('Latin American', 'Latin American'), ('Mediterranean', 'Mediterranean'), ('Middle Eastern', 'Middle Eastern'), ('Southern', 'Southern'), ('No Preference', 'No Preference')], default='No Preference', max_length=16)),
                ('cuisine_pref2', models.CharField(choices=[('Asian', 'Asian'), ('American', 'American'), ('Caribbean', 'Caribbean'), ('European', 'European'), ('Indian', 'Indian'), ('Latin American', 'Latin American'), ('Mediterranean', 'Mediterranean'), ('Middle Eastern', 'Middle Eastern'), ('Southern', 'Southern'), ('No Preference', 'No Preference')], default='No Preference', max_length=16)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='upreferences', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='accessible_restaurant.restaurant')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]