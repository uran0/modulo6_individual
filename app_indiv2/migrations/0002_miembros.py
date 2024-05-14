# Generated by Django 4.2.13 on 2024-05-10 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_indiv2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miembros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70)),
                ('apodo', models.CharField(max_length=20)),
                ('edad', models.IntegerField()),
                ('color_favorito', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
