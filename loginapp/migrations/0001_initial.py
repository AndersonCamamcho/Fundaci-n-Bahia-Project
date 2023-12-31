# Generated by Django 4.2.7 on 2023-11-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beneficiary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Identification', models.CharField(max_length=9)),
                ('birthdate', models.DateField(help_text='Por favor, introduce la fecha de cumpleaños.')),
                ('registration_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
